import logging

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import DatabaseError
from werkzeug.exceptions import InternalServerError, NotFound

from models import db, Post
from views.forms.posts import PostForm

posts_app = Blueprint("posts_app", __name__)


@posts_app.route("/", endpoint="list")
def list_posts():
    posts = Post.query.order_by(Post.updated_at.desc()).all()
    return render_template(
        "posts/list.html",
        active_page="posts",
        posts=posts,
    )


@posts_app.route("/add/", methods=["GET", "POST"], endpoint="add")
@posts_app.route("/<int:post_id>/", methods=["GET", "POST"], endpoint="details")
def add_or_update_post(post_id: int = None):
    post = None
    if post_id is not None:
        post = Post.query.get(post_id)
        if post is None:
            raise NotFound(f"Post #{post_id} not found")

    form = PostForm(obj=post)
    if request.method == "GET" or not form.validate_on_submit():
        return render_template(
            "posts/add_or_update.html",
            active_page="posts",
            form=form,
            post=post,
        )

    if post is not None:
        post.title = form.data["title"]
        post.body = form.data["body"]
    else:
        post = Post(
            title=form.data["title"],
            body=form.data["body"],
        )
        db.session.add(post)
    try:
        db.session.commit()
    except DatabaseError as ex:
        db.session.rollback()
        logging.exception("DB error: %s", ex)
        raise InternalServerError(f"Could not save post with title {post.title!r}")

    return redirect(url_for("posts_app.details", post_id=post.id))
