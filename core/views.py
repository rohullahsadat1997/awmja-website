from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import (
    SiteSettings,
    ActivityPageSettings,
    Activity,
    ActivityImpact,
    ActivityImpactSettings,
    ActivityStory,
    ActivityCTASettings,
    AboutSettings,
    AboutHighlight,
    AboutIntroduction,
    AboutStory,
    AboutMissionVision,
    AboutVisionPoint,
    AboutGoalsSettings,
    AboutGoal,
    HomeImpactSettings,
    HomeImpact,
    NewsPageSettings,
    News,
    Event,
    GalleryAlbum,
    MissionVisionSettings,
    MissionPoint,
    CoreValue,
    ApproachStep,
    Achievement,
    AchievementImpact,
  AchievementMedia,
AchievementPageSettings,
AchievementTimeline,
GoalPageSettings,
Goal,
Leader,
Article,
ArticlePageSettings,
ContactPageSettings,
 ContactMessage

)

# Create your views here.
def home(request):
    settings = SiteSettings.objects.first()

    activities = Activity.objects.filter(
        is_active=True
    ).order_by(
        "order",
        "number"
    )
    about_settings = AboutSettings.objects.first()
    about_highlights = AboutHighlight.objects.filter(
        is_active=True
    ).order_by("order")

    impact_settings = HomeImpactSettings.objects.first()
    impact_statistics = HomeImpact.objects.filter(
    is_active=True
 ).order_by("order")

    
    latest_news = News.objects.filter(
    is_active=True
).order_by("-published_at", "order")[:3]
    
    upcoming_events = Event.objects.filter(
    is_active=True,
    status="upcoming",
    is_featured=False,
).order_by("event_date", "order")[:3]
    
    gallery_albums = GalleryAlbum.objects.filter(
    is_active=True
).order_by("order", "id")[:5]

    print("DEBUG SETTINGS:", settings)
    print("DEBUG HERO:", settings.hero_title_fa)

    return render(
        request,
        "pages/index.html",
        {
            "settings": settings,
            "activities": activities,
            "about_settings": about_settings,
            "about_highlights": about_highlights,
            "impact_settings": impact_settings,
            "impact_statistics": impact_statistics,
            "latest_news": latest_news,
            "upcoming_events": upcoming_events,
            "gallery_albums": gallery_albums,
        }
    )
    
    
def about(request):
    about_settings = AboutSettings.objects.first()

    about_highlights = AboutHighlight.objects.filter(
        is_active=True
    ).order_by("order")

    about_introduction = AboutIntroduction.objects.first()

    about_stories = AboutStory.objects.filter(
        is_active=True
    ).order_by("order", "number")

    about_mission_vision = AboutMissionVision.objects.first()

    about_vision_points = AboutVisionPoint.objects.filter(
        is_active=True
    ).order_by("order", "number")

    about_goals_settings = AboutGoalsSettings.objects.first()

    about_goals = AboutGoal.objects.filter(
        is_active=True
    ).order_by("order", "number")

    return render(
        request,
        "pages/about.html",
        {
            "about_settings": about_settings,
            "about_highlights": about_highlights,
            "about_introduction": about_introduction,
            "about_stories": about_stories,
            "about_mission_vision": about_mission_vision,
            "about_vision_points": about_vision_points,
            "about_goals_settings": about_goals_settings,
            "about_goals": about_goals,
        }
    )
    
    

#SECTION MISSION
def mission_vision(request):
    mission_vision_settings = MissionVisionSettings.objects.first()

    mission_points = MissionPoint.objects.filter(
        is_active=True
    ).order_by(
        "order",
        "number"
    )

    core_values = CoreValue.objects.filter(
        is_active=True
    ).order_by(
        "order",
        "number"
    )

    approach_steps = ApproachStep.objects.filter(
        is_active=True
    ).order_by(
        "order",
        "number"
    )

    return render(request, "pages/mission.html", {
        "mission_vision_settings": mission_vision_settings,
        "mission_points": mission_points,
        "core_values": core_values,
        "approach_steps": approach_steps,
    })




def goals(request):
    goals_settings = GoalPageSettings.objects.first()
    goals = Goal.objects.filter(is_active=True).order_by("order", "number")
    featured_goals = goals.filter(is_featured=True)

    return render(request, "pages/goals.html", {
        "goals_settings": goals_settings,
        "goals": goals,
        "featured_goals": featured_goals,
    })


# activity 

def activities(request):

    activity_settings = ActivityPageSettings.objects.first()

    impact_settings = ActivityImpactSettings.objects.first()
    cta_settings = ActivityCTASettings.objects.first()

    activities = Activity.objects.filter(
        is_active=True
    ).order_by(
        "order",
        "number"
    )

    featured_activities = activities.filter(
        is_featured=True
    )

    impact_statistics = ActivityImpact.objects.filter(
        is_active=True
    ).order_by(
        "order",
        "number"
    )

    stories = ActivityStory.objects.filter(
        is_active=True
    ).order_by(
        "order",
        "number"
    )

    return render(
        request,
        "pages/activities.html",
        {
            "activity_settings": activity_settings,
            "impact_settings": impact_settings,
            "cta_settings": cta_settings,
            "activities": activities,
            "featured_activities": featured_activities,
            "impact_statistics": impact_statistics,
            "stories": stories,
        }
    )
# achivement section
def achievements(request):
    achievement_settings = AchievementPageSettings.objects.first()

    impact_statistics = AchievementImpact.objects.filter(
        is_active=True
    ).order_by("order", "id")

    achievements_list = Achievement.objects.filter(
        is_active=True
    ).order_by("order", "number")

    featured_achievements = achievements_list.filter(
        is_featured=True
    )

    timeline = AchievementTimeline.objects.filter(
        is_active=True
    ).order_by("order", "year")

    media_items = AchievementMedia.objects.filter(
        is_active=True
    ).order_by("order", "id")

    return render(
        request,
        "pages/achievements.html",
        {
            "achievement_settings": achievement_settings,
            "impact_statistics": impact_statistics,
            "achievements": achievements_list,
            "featured_achievements": featured_achievements,
            "timeline": timeline,
            "media_items": media_items,
        },
    )

#LEADERSHIP

def leadership(request):
    main_leader = Leader.objects.filter(
        is_active=True,
        is_main=True
    ).first()

    leaders = Leader.objects.filter(
        is_active=True,
        is_main=False
    ).order_by("order", "number")

    return render(request, "pages/leadership.html", {
        "main_leader": main_leader,
        "leaders": leaders,
    })
#NEWS SECTION
def news(request):
    news_settings = NewsPageSettings.objects.first()

    featured_news = News.objects.filter(
        is_active=True,
        is_featured=True
    ).order_by("-published_at", "order").first()

    latest_news = News.objects.filter(
        is_active=True
    ).order_by("-published_at", "order")

    return render(
        request,
        "pages/news.html",
        {
            "news_settings": news_settings,
            "featured_news": featured_news,
            "latest_news": latest_news,
        }
    )
    
    
    
#EVENTS SECTION
def events(request):
    events = Event.objects.filter(is_active=True)

    upcoming_events = events.filter(
        status="upcoming",
        is_featured=False
    ).order_by("event_date", "order")

    past_events = events.filter(
        status="past"
    ).order_by("-event_date", "order")

    featured_event = events.filter(
        is_featured=True
    ).order_by("order", "-event_date").first()

    schema_events = events.filter(
        status="upcoming"
    ).order_by("event_date", "order")

    return render(request, "pages/events.html", {
        "upcoming_events": upcoming_events,
        "past_events": past_events,
        "featured_event": featured_event,
        "schema_events": schema_events,
    })
    
    

#gallery SECTION
def gallery(request):
    albums = GalleryAlbum.objects.filter(
        is_active=True
    ).prefetch_related(
        "media"
    ).order_by(
        "order",
        "id"
    )

    return render(request, "pages/gallery.html", {
        "albums": albums,
    })


#ARTICLE

def articles(request):
    article_settings = ArticlePageSettings.objects.first()

    featured_article = Article.objects.filter(
        is_active=True,
        is_featured=True
    ).order_by("-published_at", "order").first()

    articles_list = Article.objects.filter(
        is_active=True
    ).order_by("-published_at", "order")

    return render(request, "pages/articles.html", {
        "article_settings": article_settings,
        "featured_article": featured_article,
        "articles": articles_list,
    })
def article_detail(request, slug):
    article = get_object_or_404(
        Article,
        slug=slug,
        is_active=True
    )

    return render(request, "pages/article-single.html", {
        "article": article,
    })


def contact(request):
    return render(request, "pages/contact.html")
#GOAL SECTION


#//////////////////////////////////////////////////////////////////////////////////////////
#CONTACT SECTION
def contact(request):

    contact_settings = ContactPageSettings.objects.first()

    error_message = None

    form_data = {
        "name": "",
        "email": "",
        "phone": "",
        "subject": "",
        "message": "",
        "consent": False,
    }

    if request.method == "POST":

        form_data["name"] = request.POST.get("name", "").strip()
        form_data["email"] = request.POST.get("email", "").strip()
        form_data["phone"] = request.POST.get("phone", "").strip()
        form_data["subject"] = request.POST.get("subject", "").strip()
        form_data["message"] = request.POST.get("message", "").strip()
        form_data["consent"] = request.POST.get("consent") == "on"

        if not form_data["name"]:
            error_message = (
                "لطفاً نام و نام خانوادگی خود را وارد کنید."
                if request.LANGUAGE_CODE == "fa"
                else "Please enter your full name."
            )

        elif not form_data["email"]:
            error_message = (
                "لطفاً ایمیل خود را وارد کنید."
                if request.LANGUAGE_CODE == "fa"
                else "Please enter your email."
            )

        elif not form_data["subject"]:
            error_message = (
                "لطفاً موضوع پیام را انتخاب کنید."
                if request.LANGUAGE_CODE == "fa"
                else "Please select a message subject."
            )

        elif not form_data["message"]:
            error_message = (
                "لطفاً پیام خود را وارد کنید."
                if request.LANGUAGE_CODE == "fa"
                else "Please enter your message."
            )

        elif not form_data["consent"]:
            error_message = (
                "لطفاً با استفاده از اطلاعات واردشده برای پاسخ‌گویی موافقت کنید."
                if request.LANGUAGE_CODE == "fa"
                else "Please agree to the use of your information for a response."
            )

        else:

            ContactMessage.objects.create(
                name=form_data["name"],
                email=form_data["email"],
                phone=form_data["phone"],
                subject=form_data["subject"],
                message=form_data["message"],
                consent=form_data["consent"],
            )

            return redirect("contact_success")

    return render(
        request,
        "pages/contact.html",
        {
            "contact_settings": contact_settings,
            "form_data": form_data,
            "error_message": error_message,
        },
    )
def contact_success(request):
    return render(request, "pages/contact-success.html")




#robot.txt
def robots_txt(request):
    content = """User-agent: *
Allow: /

Disallow: /admin/
Disallow: /i18n/
Disallow: /contact/success/

Sitemap: https://awmja.org/sitemap.xml
"""

    return HttpResponse(
        content,
        content_type="text/plain"
    )