from django.contrib import admin

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
        GalleryMedia,
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
    ContactMessage,
)



# =====================================================
# SITE SETTINGS
# =====================================================

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    list_display = (
        "site_name_fa",
        "site_name_en",
        "email",
        "updated_at",
    )

    fieldsets = (
        (
            "اطلاعات اصلی سایت",
            {
                "fields": (
                    "site_name_fa",
                    "site_name_en",
                    "description_fa",
                    "description_en",
                )
            },
        ),

        (
            "Hero - صفحه اصلی",
            {
                "fields": (
                    "hero_eyebrow_fa",
                    "hero_eyebrow_en",
                    "hero_title_fa",
                    "hero_title_en",
                    "hero_text_fa",
                    "hero_text_en",
                    "hero_about_button_fa",
                    "hero_about_button_en",
                    "hero_join_button_fa",
                    "hero_join_button_en",
                )
            },
        ),

        (
            "تصویر و نشان Hero",
            {
                "fields": (
                    "hero_image",
                    "hero_image_alt_fa",
                    "hero_image_alt_en",
                    "hero_badge_title",
                    "hero_badge_text_fa",
                    "hero_badge_text_en",
                )
            },
        ),

        (
            "اطلاعات تماس",
            {
                "fields": (
                    "email",
                    "phone",
                    "address_fa",
                    "address_en",
                )
            },
        ),

        (
            "شبکه‌های اجتماعی",
            {
                "fields": (
                    "facebook",
                    "instagram",
                    "linkedin",
                )
            },
        ),
    )


# =====================================================
# ACTIVITY PAGE SETTINGS
# =====================================================

@admin.register(ActivityPageSettings)
class ActivityPageSettingsAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Hero فعالیت‌ها",
            {
                "fields": (
                    "hero_kicker_fa",
                    "hero_kicker_en",
                    "hero_title_fa",
                    "hero_title_en",
                    "hero_lead_fa",
                    "hero_lead_en",
                    "hero_text_fa",
                    "hero_text_en",
                )
            },
        ),

        (
            "تصویر Hero",
            {
                "fields": (
                    "hero_image",
                    "hero_image_alt_fa",
                    "hero_image_alt_en",
                )
            },
        ),

        (
            "نقل‌قول و آمار",
            {
                "fields": (
                    "hero_quote_fa",
                    "hero_quote_en",
                    "hero_stat_number",
                    "hero_stat_label_fa",
                    "hero_stat_label_en",
                )
            },
        ),
    )


# =====================================================
# ACTIVITIES
# =====================================================

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):

    list_display = (
        "number",
        "title_fa",
        "title_en",
        "is_active",
        "order",
        "updated_at",
       "category_fa",
        "is_featured",
   
    )

    list_display_links = (
        "number",
        "title_fa",
    )

    list_editable = (
        "is_active",
        "order",
    )

    list_filter = (
        "is_active",
          "is_featured",
    )

    search_fields = (
        "title_fa",
        "title_en",
        "category_fa",
        "category_en",
        "description_fa",
        "description_en",
    )

    ordering = (
        "order",
        "number",
    )

    fieldsets = (
        (
            "اطلاعات اصلی فعالیت",
            {
                "fields": (
                    "number",
                    "category_fa",
                    "category_en",
                    "title_fa",
                    "title_en",
                    "description_fa",
                    "description_en",
                )
            },
        ),

        (
            "آیکون",
            {
                "fields": (
                    "icon",
                    "icon_style",
                )
            },
        ),

        (
            "تصویر فعالیت",
            {
                "fields": (
                    "image",
                    "image_alt_fa",
                    "image_alt_en",
                )
            },
        ),

        (
            "لینک",
            {
                "fields": (
                    "link",
                )
            },
        ),

       (
    "وضعیت و ترتیب",
    {
        "fields": (
            "is_active",
            "is_featured",
            "order",
        )
    },
),
    )
    

@admin.register(ActivityImpact)
class ActivityImpactAdmin(admin.ModelAdmin):

    list_display = (
        "number",
        "value",
        "label_fa",
        "label_en",
        "is_active",
        "order",
        "updated_at",
    )

    list_display_links = (
        "number",
        "label_fa",
    )

    list_editable = (
        "value",
        "is_active",
        "order",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "label_fa",
        "label_en",
    )

    ordering = (
        "order",
        "number",
    )

    fieldsets = (
        (
            "اطلاعات آمار",
            {
                "fields": (
                    "number",
                    "value",
                    "label_fa",
                    "label_en",
                )
            },
        ),

        (
            "وضعیت و ترتیب",
            {
                "fields": (
                    "is_active",
                    "order",
                )
            },
        ),
    )
    
# =====================================================
# ACTIVITY IMPACT SETTINGS
# =====================================================

@admin.register(ActivityImpactSettings)
class ActivityImpactSettingsAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "برچسب بخش",
            {
                "fields": (
                    "kicker_fa",
                    "kicker_en",
                )
            },
        ),

        (
            "عنوان بخش",
            {
                "fields": (
                    "title_fa",
                    "title_en",
                )
            },
        ),

        (
            "توضیحات بخش",
            {
                "fields": (
                    "text_fa",
                    "text_en",
                )
            },
        ),

        (
            "دکمه",
            {
                "fields": (
                    "button_fa",
                    "button_en",
                )
            },
        ),
    )

    list_display = (
        "title_fa",
        "title_en",
    )


@admin.register(ActivityCTASettings)
class ActivityCTASettingsAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "برچسب بخش",
            {
                "fields": (
                    "kicker_fa",
                    "kicker_en",
                )
            },
        ),

        (
            "عنوان بخش",
            {
                "fields": (
                    "title_fa",
                    "title_en",
                )
            },
        ),

        (
            "توضیحات بخش",
            {
                "fields": (
                    "text_fa",
                    "text_en",
                )
            },
        ),

        (
            "دکمه اصلی",
            {
                "fields": (
                    "primary_button_fa",
                    "primary_button_en",
                    "primary_link",
                )
            },
        ),

        (
            "دکمه دوم",
            {
                "fields": (
                    "secondary_button_fa",
                    "secondary_button_en",
                    "secondary_link",
                )
            },
        ),
    )

    list_display = (
        "title_fa",
        "title_en",
    )
    
@admin.register(ActivityStory)
class ActivityStoryAdmin(admin.ModelAdmin):

    list_display = (
        "number",
        "title_fa",
        "title_en",
        "category_fa",
        "is_active",
        "order",
        "updated_at",
    )

    list_display_links = (
        "number",
        "title_fa",
    )

    list_editable = (
        "is_active",
        "order",
    )

    list_filter = (
        "is_active",
        "category_fa",
    )

    search_fields = (
        "title_fa",
        "title_en",
        "category_fa",
        "category_en",
        "description_fa",
        "description_en",
    )

    ordering = (
        "order",
        "number",
    )

    fieldsets = (

        (
            "اطلاعات اصلی روایت",
            {
                "fields": (
                    "number",
                    "category_fa",
                    "category_en",
                    "title_fa",
                    "title_en",
                    "description_fa",
                    "description_en",
                )
            },
        ),

        (
            "تصویر روایت",
            {
                "fields": (
                    "image",
                    "image_alt_fa",
                    "image_alt_en",
                )
            },
        ),

        (
            "لینک",
            {
                "fields": (
                    "link",
                )
            },
        ),

        (
            "وضعیت و ترتیب",
            {
                "fields": (
                    "is_active",
                    "order",
                )
            },
        ),
    )
    
# About section
   
    # =====================================================
# ABOUT SETTINGS
# =====================================================

@admin.register(AboutSettings)
class AboutSettingsAdmin(admin.ModelAdmin):

    fieldsets = (

        (
            "پیش‌نمایش About در صفحه اصلی — فارسی",
            {
                "fields": (
                    "preview_kicker_fa",
                    "preview_title_fa",
                    "preview_text_fa",
                    "preview_image_alt_fa",
                    "preview_button_fa",
                    "foundation_label_fa",
                )
            },
        ),

        (
            "پیش‌نمایش About در صفحه اصلی — English",
            {
                "fields": (
                    "preview_kicker_en",
                    "preview_title_en",
                    "preview_text_en",
                    "preview_image_alt_en",
                    "preview_button_en",
                    "foundation_label_en",
                )
            },
        ),

        (
            "تصویر و اطلاعات پایه",
            {
                "fields": (
                    "preview_image",
                    "preview_link",
                    "foundation_year",
                )
            },
        ),

        (
            "About Hero — فارسی",
            {
                "fields": (
                    "hero_kicker_fa",
                    "hero_title_fa",
                    "hero_text_fa",
                    "hero_image_alt_fa",
                    "hero_badge_top_fa",
                    "hero_badge_bottom_fa",
                )
            },
        ),

        (
            "About Hero — English",
            {
                "fields": (
                    "hero_kicker_en",
                    "hero_title_en",
                    "hero_text_en",
                    "hero_image_alt_en",
                    "hero_badge_top_en",
                    "hero_badge_bottom_en",
                )
            },
        ),

        (
            "تصویر About Hero",
            {
                "fields": (
                    "hero_image",
                )
            },
        ),
    )

    list_display = (
        "preview_title_fa",
        "preview_title_en",
        "foundation_year",
    )


# =====================================================
# ABOUT HIGHLIGHTS
# =====================================================

@admin.register(AboutHighlight)
class AboutHighlightAdmin(admin.ModelAdmin):

    fieldsets = (

        (
            "محتوای فارسی",
            {
                "fields": (
                    "title_fa",
                    "description_fa",
                )
            },
        ),

        (
            "English Content",
            {
                "fields": (
                    "title_en",
                    "description_en",
                )
            },
        ),

        (
            "نمایش",
            {
                "fields": (
                    "icon",
                    "order",
                    "is_active",
                )
            },
        ),
    )

    list_display = (
        "title_fa",
        "title_en",
        "order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title_fa",
        "title_en",
        "description_fa",
        "description_en",
    )

    ordering = (
        "order",
    )

@admin.register(AboutIntroduction)
class AboutIntroductionAdmin(admin.ModelAdmin):
    fieldsets = (
        ("محتوای فارسی", {
            "fields": (
                "kicker_fa",
                "title_fa",
                "lead_fa",
                "text_fa",
            )
        }),

        ("English Content", {
            "fields": (
                "kicker_en",
                "title_en",
                "intro_en",
                "lead_en",
                "text_en",
            )
        }),

        ("بخش برجسته", {
            "fields": (
                "highlight_name",
                "highlight_text",
            )
        }),
    )

    list_display = (
        "title_fa",
        "title_en",
    )

@admin.register(AboutStory)
class AboutStoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ("اطلاعات روایت", {
            "fields": (
                "number",
                "date_main",
                "date_sub",
                "order",
                "is_active",
            )
        }),

        ("محتوای فارسی", {
            "fields": (
                "title_fa",
                "description_fa",
            )
        }),

        ("English Content", {
            "fields": (
                "title_en",
                "description_en",
            )
        }),

        ("تصویر", {
            "fields": (
                "image",
                "image_alt_fa",
                "image_alt_en",
            )
        }),
    )

    list_display = (
        "number",
        "title_fa",
        "date_main",
        "date_sub",
        "order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title_fa",
        "title_en",
        "description_fa",
        "description_en",
    )

    ordering = (
        "order",
        "number",
    )
    
@admin.register(AboutMissionVision)
class AboutMissionVisionAdmin(admin.ModelAdmin):
    fieldsets = (
        ("اطلاعات اصلی بخش", {
            "fields": (
                "kicker_fa",
                "title_fa",
                "intro_fa",
            )
        }),

        ("Main Section — English", {
            "fields": (
                "kicker_en",
                "title_en",
                "intro_en",
            )
        }),

        ("مأموریت — فارسی", {
            "fields": (
                "mission_number",
                "mission_label_fa",
                "mission_icon",
                "mission_title_fa",
                "mission_lead_fa",
                "mission_text_fa",
                "mission_footer_1",
                "mission_footer_2",
                "mission_footer_3",
            )
        }),

        ("Mission — English", {
            "fields": (
                "mission_label_en",
                "mission_title_en",
                "mission_lead_en",
                "mission_text_en",
            )
        }),

        ("چشم‌انداز — فارسی", {
            "fields": (
                "vision_number",
                "vision_label_fa",
                "vision_icon",
                "vision_title_fa",
                "vision_lead_fa",
                "vision_footer_1",
                "vision_footer_2",
                "vision_footer_3",
            )
        }),

        ("Vision — English", {
            "fields": (
                "vision_label_en",
                "vision_title_en",
                "vision_lead_en",
            )
        }),
    )

    list_display = (
        "title_fa",
        "title_en",
    )
    
@admin.register(AboutVisionPoint)
class AboutVisionPointAdmin(admin.ModelAdmin):
    fieldsets = (
        ("محتوای فارسی", {
            "fields": (
                "number",
                "title_fa",
            )
        }),

        ("English Content", {
            "fields": (
                "title_en",
            )
        }),

        ("نمایش", {
            "fields": (
                "order",
                "is_active",
            )
        }),
    )

    list_display = (
        "number",
        "title_fa",
        "title_en",
        "order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title_fa",
        "title_en",
    )

    ordering = (
        "order",
        "number",
    )
    
@admin.register(AboutGoalsSettings)
class AboutGoalsSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("محتوای فارسی", {
            "fields": (
                "kicker_fa",
                "title_fa",
                "intro_fa",
            )
        }),

        ("English Content", {
            "fields": (
                "kicker_en",
                "title_en",
                "intro_en",
            )
        }),

        ("پایان بخش", {
            "fields": (
                "closing_name",
                "closing_text_fa",
                "closing_text_en",
            )
        }),
    )

    list_display = (
        "title_fa",
        "title_en",
    )
    
@admin.register(AboutGoal)
class AboutGoalAdmin(admin.ModelAdmin):
    fieldsets = (
        ("اطلاعات هدف", {
            "fields": (
                "number",
                "icon",
                "order",
                "is_active",
            )
        }),

        ("محتوای فارسی", {
            "fields": (
                "title_fa",
                "description_fa",
            )
        }),

        ("English Content", {
            "fields": (
                "title_en",
                "description_en",
            )
        }),
    )

    list_display = (
        "number",
        "title_fa",
        "title_en",
        "order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title_fa",
        "title_en",
        "description_fa",
        "description_en",
    )

    ordering = (
        "order",
        "number",
    )
    
    
#home impact////////////////////////////////////////////////////////////////////////////
@admin.register(HomeImpactSettings)
class HomeImpactSettingsAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "محتوای فارسی",
            {
                "fields": (
                    "kicker_fa",
                    "title_fa",
                    "text_fa",
                )
            }
        ),
        (
            "English Content",
            {
                "fields": (
                    "kicker_en",
                    "title_en",
                    "text_en",
                )
            }
        ),
    )

    list_display = (
        "title_fa",
        "title_en",
    )


@admin.register(HomeImpact)
class HomeImpactAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "اطلاعات آمار",
            {
                "fields": (
                    "number",
                    "order",
                    "is_active",
                )
            }
        ),
        (
            "محتوای فارسی",
            {
                "fields": (
                    "label_fa",
                )
            }
        ),
        (
            "English Content",
            {
                "fields": (
                    "label_en",
                )
            }
        ),
    )

    list_display = (
        "number",
        "label_fa",
        "label_en",
        "order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "number",
        "label_fa",
        "label_en",
    )

    ordering = (
        "order",
    )

#NEWS PAGE SETTINGS
@admin.register(NewsPageSettings)
class NewsPageSettingsAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Hero — فارسی",
            {
                "fields": (
                    "hero_kicker_fa",
                    "hero_title_fa",
                    "hero_text_fa",
                )
            }
        ),
        (
            "Hero — English",
            {
                "fields": (
                    "hero_kicker_en",
                    "hero_title_en",
                    "hero_text_en",
                )
            }
        ),

        (
            "خبر ویژه — فارسی",
            {
                "fields": (
                    "featured_kicker_fa",
                    "featured_title_fa",
                )
            }
        ),
        (
            "Featured News — English",
            {
                "fields": (
                    "featured_kicker_en",
                    "featured_title_en",
                )
            }
        ),

        (
            "آخرین اخبار — فارسی",
            {
                "fields": (
                    "latest_kicker_fa",
                    "latest_title_fa",
                    "latest_text_fa",
                )
            }
        ),
        (
            "Latest News — English",
            {
                "fields": (
                    "latest_kicker_en",
                    "latest_title_en",
                    "latest_text_en",
                )
            }
        ),

        (
            "رسانه و منابع — فارسی",
            {
                "fields": (
                    "media_kicker_fa",
                    "media_title_fa",
                    "media_text_fa",
                    "media_note_title_fa",
                    "media_note_text_fa",
                )
            }
        ),
        (
            "Media & Sources — English",
            {
                "fields": (
                    "media_kicker_en",
                    "media_title_en",
                    "media_text_en",
                    "media_note_title_en",
                    "media_note_text_en",
                )
            }
        ),

        (
            "آرشیو اخبار — فارسی",
            {
                "fields": (
                    "archive_kicker_fa",
                    "archive_title_fa",
                    "archive_text_fa",
                    "archive_button_fa",
                )
            }
        ),
        (
            "News Archive — English",
            {
                "fields": (
                    "archive_kicker_en",
                    "archive_title_en",
                    "archive_text_en",
                    "archive_button_en",
                )
            }
        ),

        (
            "لینک آرشیو",
            {
                "fields": (
                    "archive_link",
                )
            }
        ),
    )

    list_display = (
        "hero_title_fa",
        "hero_title_en",
    )
    
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("اطلاعات اصلی", {
            "fields": (
                "category",
                "published_at",
                "source",
                "source_url",
                 "external_url",
                "slug",
            )
        }),
        ("فارسی", {
            "fields": (
                "title_fa",
                "excerpt_fa",
                "content_fa",
                "category_fa",
            )
        }),
        ("English", {
            "fields": (
                "title_en",
                "excerpt_en",
                "content_en",
                "category_en",
            )
        }),
        ("تصویر", {
            "fields": (
                "image",
                "image_alt_fa",
                "image_alt_en",
            )
        }),
        ("نمایش", {
            "fields": (
                "is_featured",
                "is_active",
                "order",
            )
        }),
    )

    list_display = (
        "title_fa",
        "category",
        "published_at",
        "is_featured",
        "is_active",
        "order",
    )

    list_filter = (
        "category",
        "is_featured",
        "is_active",
        "published_at",
    )

    search_fields = (
        "title_fa",
        "title_en",
        "excerpt_fa",
        "excerpt_en",
        "content_fa",
        "content_en",
        "source",
    )

    prepopulated_fields = {
        "slug": ("title_fa",)
    }

    ordering = (
        "-published_at",
        "order",
    )
    
#EVENTS
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title_fa",
        "category",
        "event_date",
        "status",
        "is_featured",
        "is_active",
        "order",
    )

    list_filter = (
        "status",
        "category",
        "is_featured",
        "is_active",
        "event_date",
    )

    search_fields = (
        "title_fa",
        "title_en",
        "description_fa",
        "description_en",
    )

    ordering = (
        "-event_date",
        "order",
    )

    fieldsets = (
        (
            "اطلاعات اصلی",
            {
                "fields": (
                    "title_fa",
                    "title_en",
                    "category",
                    "category_fa",
                    "category_en",
                    "event_date",
                    "status",
                    "location_fa",
                    "location_en",
                )
            },
        ),
        (
            "توضیحات",
            {
                "fields": (
                    "description_fa",
                    "description_en",
                )
            },
        ),
        (
            "تصویر",
            {
                "fields": (
                    "image",
                    "image_alt_fa",
                    "image_alt_en",
                )
            },
        ),
        (
            "لینک و نمایش",
            {
                "fields": (
                    "external_url",
                    "is_featured",
                    "is_active",
                    "order",
                )
            },
        ),
    )
#SECTION GALLERY
from .models import GalleryAlbum, GalleryMedia


class GalleryMediaInline(admin.TabularInline):
    model = GalleryMedia
    extra = 1
    fields = (
        "media_type",
        "image",
        "video",
        "title_fa",
        "title_en",
        "description_fa",
        "description_en",
        "image_alt_fa",
        "image_alt_en",
        "order",
        "is_active",
    )


@admin.register(GalleryAlbum)
class GalleryAlbumAdmin(admin.ModelAdmin):

    list_display = (
        "title_fa",
        "category",
        "order",
        "is_active",
    )

    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "title_fa",
        "title_en",
        "description_fa",
        "description_en",
    )

    ordering = (
        "order",
        "id",
    )

    fieldsets = (
        (
            "اطلاعات اصلی",
            {
                "fields": (
                    "title_fa",
                    "title_en",
                    "category",
                    "category_fa",
                    "category_en",
                    "description_fa",
                    "description_en",
                )
            },
        ),

        (
            "تصویر روی جلد آلبوم",
            {
                "fields": (
                    "cover_image",
                    "cover_alt_fa",
                    "cover_alt_en",
                )
            },
        ),

        (
            "نمایش",
            {
                "fields": (
                    "order",
                    "is_active",
                )
            },
        ),
    )

    inlines = [
        GalleryMediaInline,
    ]
#MISSION & VISION SECTION
@admin.register(MissionVisionSettings)
class MissionVisionSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Hero", {
            "fields": (
                "hero_kicker_fa",
                "hero_kicker_en",
                "hero_title_fa",
                "hero_title_en",
                "hero_highlight_fa",
                "hero_highlight_en",
                "hero_text_fa",
                "hero_text_en",
            )
        }),

        ("Mission", {
            "fields": (
                "mission_kicker_fa",
                "mission_kicker_en",
                "mission_title_fa",
                "mission_title_en",
                "mission_lead_fa",
                "mission_lead_en",
                "mission_text_fa",
                "mission_text_en",
                "mission_text_2_fa",
                "mission_text_2_en",
                "mission_image",
                "mission_image_alt_fa",
                "mission_image_alt_en",
                "mission_badge_title_fa",
                "mission_badge_title_en",
                "mission_badge_text_fa",
                "mission_badge_text_en",
            )
        }),

        ("Vision", {
            "fields": (
                "vision_kicker_fa",
                "vision_kicker_en",
                "vision_title_fa",
                "vision_title_en",
                "vision_lead_fa",
                "vision_lead_en",
                "vision_text_fa",
                "vision_text_en",
                "vision_statement_fa",
                "vision_statement_en",
            )
        }),

        ("Final CTA", {
            "fields": (
                "cta_kicker_fa",
                "cta_kicker_en",
                "cta_title_fa",
                "cta_title_en",
                "cta_text_fa",
                "cta_text_en",
                "cta_button_fa",
                "cta_button_en",
                "cta_button_2_fa",
                "cta_button_2_en",
            )
        }),
    )


@admin.register(MissionPoint)
class MissionPointAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "title_fa",
        "order",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = (
        "title_fa",
        "title_en",
        "description_fa",
        "description_en",
    )
    ordering = ("order", "number")


@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "title_fa",
        "order",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = (
        "title_fa",
        "title_en",
        "description_fa",
        "description_en",
    )
    ordering = ("order", "number")


@admin.register(ApproachStep)
class ApproachStepAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "title_fa",
        "order",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = (
        "title_fa",
        "title_en",
        "description_fa",
        "description_en",
    )
    ordering = ("order", "number")

#Achivement
@admin.register(AchievementPageSettings)
class AchievementPageSettingsAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Hero",
            {
                "fields": (
                    "hero_kicker_fa",
                    "hero_kicker_en",
                    "hero_title_fa",
                    "hero_title_en",
                    "hero_highlight_fa",
                    "hero_highlight_en",
                    "hero_text_fa",
                    "hero_text_en",
                    "hero_button_fa",
                    "hero_button_en",
                    "hero_button_2_fa",
                    "hero_button_2_en",
                )
            },
        ),

        (
            "Impact Intro",
            {
                "fields": (
                    "intro_kicker_fa",
                    "intro_kicker_en",
                    "intro_title_fa",
                    "intro_title_en",
                    "intro_highlight_fa",
                    "intro_highlight_en",
                    "intro_text_fa",
                    "intro_text_en",
                )
            },
        ),

        (
            "Key Achievements",
            {
                "fields": (
                    "achievements_kicker_fa",
                    "achievements_kicker_en",
                    "achievements_title_fa",
                    "achievements_title_en",
                    "achievements_text_fa",
                    "achievements_text_en",
                )
            },
        ),

        (
            "Timeline",
            {
                "fields": (
                    "timeline_kicker_fa",
                    "timeline_kicker_en",
                    "timeline_title_fa",
                    "timeline_title_en",
                    "timeline_text_fa",
                    "timeline_text_en",
                )
            },
        ),

        (
            "Media & Recognition",
            {
                "fields": (
                    "media_kicker_fa",
                    "media_kicker_en",
                    "media_title_fa",
                    "media_title_en",
                    "media_highlight_fa",
                    "media_highlight_en",
                    "media_text_fa",
                    "media_text_en",
                )
            },
        ),

        (
            "Documentation",
            {
                "fields": (
                    "evidence_kicker_fa",
                    "evidence_kicker_en",
                    "evidence_title_fa",
                    "evidence_title_en",
                    "evidence_highlight_fa",
                    "evidence_highlight_en",
                    "evidence_text_fa",
                    "evidence_text_en",
                )
            },
        ),

        (
            "Final CTA",
            {
                "fields": (
                    "cta_kicker_fa",
                    "cta_kicker_en",
                    "cta_title_fa",
                    "cta_title_en",
                    "cta_highlight_fa",
                    "cta_highlight_en",
                    "cta_text_fa",
                    "cta_text_en",
                    "cta_button_fa",
                    "cta_button_en",
                )
            },
        ),
    )

@admin.register(AchievementImpact)
class AchievementImpactAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "label_fa",
        "suffix",
        "order",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = (
        "number",
        "label_fa",
        "label_en",
        "stat_key",
    )
    ordering = ("order", "id")

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "title_fa",
        "category",
        "year",
        "is_featured",
        "is_active",
        "order",
    )
    list_filter = (
        "category",
        "year",
        "is_featured",
        "is_active",
    )
    search_fields = (
        "title_fa",
        "title_en",
        "description_fa",
        "description_en",
        "category_fa",
        "category_en",
    )
    ordering = ("order", "number")

@admin.register(AchievementTimeline)
class AchievementTimelineAdmin(admin.ModelAdmin):
    list_display = (
        "year",
        "number",
        "title_fa",
        "order",
        "is_active",
    )
    list_filter = (
        "year",
        "is_active",
    )
    search_fields = (
        "title_fa",
        "title_en",
        "description_fa",
        "description_en",
    )
    ordering = ("order", "year")

@admin.register(AchievementMedia)
class AchievementMediaAdmin(admin.ModelAdmin):
    list_display = (
        "title_fa",
        "source_fa",
        "media_type",
        "order",
        "is_active",
    )
    list_filter = (
        "media_type",
        "is_active",
    )
    search_fields = (
        "title_fa",
        "title_en",
        "source_fa",
        "source_en",
    )
    ordering = ("order", "id")

#goal section
@admin.register(GoalPageSettings)
class GoalPageSettingsAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Hero",
            {
                "fields": (
                    "hero_kicker_fa",
                    "hero_kicker_en",
                    "hero_title_fa",
                    "hero_title_en",
                    "hero_text_fa",
                    "hero_text_en",
                )
            },
        ),

        (
            "Main Goals",
            {
                "fields": (
                    "goals_kicker_fa",
                    "goals_kicker_en",
                    "goals_title_fa",
                    "goals_title_en",
                    "goals_text_fa",
                    "goals_text_en",
                )
            },
        ),

        (
            "Commitment",
            {
                "fields": (
                    "commitment_kicker_fa",
                    "commitment_kicker_en",
                    "commitment_title_fa",
                    "commitment_title_en",
                    "commitment_highlight_fa",
                    "commitment_highlight_en",
                    "commitment_text_fa",
                    "commitment_text_en",
                )
            },
        ),

        (
            "CTA",
            {
                "fields": (
                    "cta_kicker_fa",
                    "cta_kicker_en",
                    "cta_title_fa",
                    "cta_title_en",
                    "cta_highlight_fa",
                    "cta_highlight_en",
                    "cta_button_fa",
                    "cta_button_en",
                )
            },
        ),
    )
    
@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):

    list_display = (
        "number",
        "title_fa",
        "category",
        "is_featured",
        "is_active",
        "order",
    )

    list_filter = (
        "category",
        "is_featured",
        "is_active",
    )

    search_fields = (
        "title_fa",
        "title_en",
        "description_fa",
        "description_en",
    )

    ordering = (
        "order",
        "number",
    )
#LEADERSHIP
@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):

    list_display = (
        "number",
        "name_fa",
        "role_fa",
        "is_main",
        "is_active",
        "order",
    )

    list_filter = (
        "is_main",
        "is_active",
    )

    search_fields = (
        "name_fa",
        "name_en",
        "role_fa",
        "role_en",
        "bio_fa",
        "bio_en",
    )

    ordering = (
        "order",
        "number",
    )
    
#ACRTICLES
@admin.register(ArticlePageSettings)
class ArticlePageSettingsAdmin(admin.ModelAdmin):

    fieldsets = (

        ("Hero", {
            "fields": (
                "hero_kicker_fa",
                "hero_kicker_en",
                "hero_title_fa",
                "hero_title_en",
                "hero_highlight_fa",
                "hero_highlight_en",
                "hero_text_fa",
                "hero_text_en",
            )
        }),

        ("Featured Article", {
            "fields": (
                "featured_kicker_fa",
                "featured_kicker_en",
                "featured_title_fa",
                "featured_title_en",
                "featured_text_fa",
                "featured_text_en",
            )
        }),

        ("Articles", {
            "fields": (
                "articles_kicker_fa",
                "articles_kicker_en",
                "articles_title_fa",
                "articles_title_en",
                "articles_highlight_fa",
                "articles_highlight_en",
                "articles_text_fa",
                "articles_text_en",
            )
        }),

        ("CTA", {
            "fields": (
                "cta_kicker_fa",
                "cta_kicker_en",
                "cta_title_fa",
                "cta_title_en",
                "cta_highlight_fa",
                "cta_highlight_en",
                "cta_text_fa",
                "cta_text_en",
                "cta_button_fa",
                "cta_button_en",
            )
        }),
    )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        "title_fa",
        "category",
        "published_at",
        "is_featured",
        "is_active",
        "order",
    )

    list_filter = (
        "category",
        "is_featured",
        "is_active",
    )

    search_fields = (
        "title_fa",
        "title_en",
        "excerpt_fa",
        "excerpt_en",
        "content_fa",
        "content_en",
    )

    prepopulated_fields = {
        "slug": ("title_fa",)
    }

    ordering = (
        "-published_at",
        "order",
    )

#ADMIN SECTION
@admin.register(ContactPageSettings)
class ContactPageSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Hero", {
            "fields": (
                "hero_kicker_fa",
                "hero_kicker_en",
                "hero_title_fa",
                "hero_title_en",
                "hero_highlight_fa",
                "hero_highlight_en",
                "hero_text_fa",
                "hero_text_en",
            )
        }),

        ("Contact Information", {
            "fields": (
                "email",
                "whatsapp_number",
                "whatsapp_url",
                "phone_number",
                "phone_url",
                "location_fa",
                "location_en",
            )
        }),

        ("Contact Form Introduction", {
            "fields": (
                "form_kicker_fa",
                "form_kicker_en",
                "form_title_fa",
                "form_title_en",
                "form_highlight_fa",
                "form_highlight_en",
                "form_text_fa",
                "form_text_en",
                "privacy_note_fa",
                "privacy_note_en",
            )
        }),

        ("Join / Support", {
            "fields": (
                "join_kicker_fa",
                "join_kicker_en",
                "join_title_fa",
                "join_title_en",
                "join_text_fa",
                "join_text_en",
                "join_button_fa",
                "join_button_en",
                "email_button_fa",
                "email_button_en",
            )
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "status",
        "created_at",
    )

    list_filter = (
        "subject",
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "message",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)