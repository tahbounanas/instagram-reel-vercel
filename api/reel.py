from instaloader import Instaloader, Post
import json

def handler(request):
    try:
        query = request.get("query", {})
        url = query.get("url", "")
        if not url:
            return {"statusCode": 400, "body": json.dumps({"error": "Missing URL"})}

        shortcode = url.rstrip('/').split('/')[-1]
        L = Instaloader()
        post = Post.from_shortcode(L.context, shortcode)

        data = {
            "user": post.owner_username,
            "video_url": post.video_url,
            "caption": post.caption or "Enjoy this reel"
        }
        return {"statusCode": 200, "body": json.dumps(data)}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
