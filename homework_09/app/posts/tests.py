from django.test import TestCase
from django.urls import reverse
from datetime import datetime

from .models import Post


class PostListViewTestCase(TestCase):
    def setUp(self):
        self.post_data = {
            "title": "Test post",
            "body": "Test body text",
        }
        self.post2_data = {
            "title": "Test post 2",
            "body": "Test body text 2",
        }
        return super().setUp()

    def test_no_posts(self):
        response = self.client.get(reverse("posts:list"))
        self.assertTemplateUsed(response, "posts/list.html")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts found")
        self.assertEqual(response.context["active_page"], "posts")
        self.assertQuerysetEqual(response.context["posts"], [])

    def test_list_one_post(self):
        post = Post.objects.create(**self.post_data)
        response = self.client.get(reverse("posts:list"))
        self.assertContains(response, post.body)
        self.assertEqual(len(response.context["posts"]), 1)
        self.assertQuerysetEqual(response.context["posts"], [post])
        post.delete()

    def test_list_two_posts(self):
        post = Post.objects.create(**self.post_data)
        post2 = Post.objects.create(**self.post2_data)
        response = self.client.get(reverse("posts:list"))
        self.assertEqual(len(response.context["posts"]), 2)
        self.assertQuerysetEqual(response.context["posts"], [post2, post])
        post.delete()
        post2.delete()


class PostCreateViewTestCase(TestCase):
    def setUp(self):
        self.post_data = {
            "title": "Test new post",
            "body": "Test body text",
        }
        return super().setUp()

    def test_add_post_get(self):
        response = self.client.get(reverse("posts:add"))
        self.assertTemplateUsed(response, "posts/add_or_update.html")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New post")
        self.assertContains(response, "Back to Posts")
        self.assertEqual(response.context["active_page"], "posts")

    def test_add_post(self):
        response = self.client.post(reverse("posts:add"), data=self.post_data)
        self.assertEqual(response.status_code, 302)
        post = Post.objects.get(title=self.post_data["title"])
        self.assertIsInstance(post, Post)
        self.assertIsInstance(post.created_at, datetime)
        self.assertIsInstance(post.updated_at, datetime)
        post.delete()


class PostUpdateViewTestCase(TestCase):
    def setUp(self):
        self.post_data = {
            "title": "Test post",
            "body": "Test body text",
        }
        self.post = Post.objects.create(**self.post_data)
        self.post_new_title = self.post_data["title"] + " updated"
        return super().setUp()

    def test_details_post_get(self):
        response = self.client.get(reverse("posts:details", args=(self.post.pk,)))
        self.assertTemplateUsed(response, "posts/add_or_update.html")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"Post #{self.post.pk}")
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)
        self.assertContains(response, "Back to Posts")
        self.assertEqual(response.context["active_page"], "posts")
        self.assertEqual(response.context["post"], self.post)

    def test_details_post_not_found(self):
        response = self.client.get(reverse("posts:details", args=(0,)))
        self.assertEqual(response.status_code, 404)

    def test_details_post_update(self):
        response = self.client.post(
            reverse("posts:details", args=(self.post.pk,)),
            data={"title": self.post_new_title, "body": self.post.body},
        )
        self.assertEqual(response.status_code, 302)
        updated_post = Post.objects.get(pk=self.post.pk)
        self.assertIsInstance(updated_post, Post)
        self.assertGreater(updated_post.updated_at, updated_post.created_at)
        self.assertEqual(updated_post.title, self.post_new_title)
        self.assertEqual(updated_post.body, self.post.body)

    def tearDown(self):
        self.post.delete()
        return super().tearDown()
