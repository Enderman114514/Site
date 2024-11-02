from django.shortcuts import render
from re import compile

from .models import Comment
from .forms import CommentForm

# Create your views here.

rep_link_pattern = compile(r"({{ (link) (.*?) }})")
rep_img_pattern = compile(r"({{ (image) (.*?) }})")

EESWES = [
    "云雨工作室官方",    "cloudrain studio - official",
    "enderman114514", "enderman·114514", "enderman",
    "曾志干",          "drant",           "drant114514",
    "泰伦卢",          "james",           "james114514",
    "郑黄干",          "gan",             "gan114514",
    "洛言",            "lynn",            "lynn57257",
    "刑天",            "xingtian",        "xingtian114514",
    "付喵",            "fumiaow",
    "鳥爆",            "baoniao",
    "雕雕",            "diaoeagle",
    "月月鸟",          "liaobird",
]

def home(request):
    comments = Comment.objects.order_by("-date_added")

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            if new_comment.owner.lower() in EESWES and request.user and request.user.id != 1:
                pass
            else:
                new_comment.content.replace("<", "&lt;")
                new_comment.content.replace(">", "&gt;")

                src = rep_img_pattern.findall(new_comment.content) + rep_link_pattern.findall(new_comment.content)
                # print(src)
                for found in src:
                    if found[1] == "link":
                        new_comment.content.replace(found[0], f"<a href='{found[2]}'>🔗链接</a>")
                    if found[1] == "image":
                        new_comment.content.replace(found[0], f"<img src='{found[2]}'>")

                new_comment.save()
            form = CommentForm()
            # return redirect('e_site:index')

    return render(request, "e_site/index.html", {"form": form, "comments": comments})