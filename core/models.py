
from django.db import models


class SiteSettings(models.Model):


    # =====================================================
    # GENERAL SITE SETTINGS
    # =====================================================

    site_name_fa = models.CharField(
        max_length=200
    )

    site_name_en = models.CharField(
        max_length=200
    )

    description_fa = models.TextField(
        blank=True
    )

    description_en = models.TextField(
        blank=True
    )


    # =====================================================
    # HERO CONTENT
    # =====================================================

    hero_eyebrow_fa = models.CharField(
        max_length=200,
        blank=True
    )

    hero_eyebrow_en = models.CharField(
        max_length=200,
        blank=True
    )

    hero_title_fa = models.CharField(
        max_length=300,
        blank=True
    )

    hero_title_en = models.CharField(
        max_length=300,
        blank=True
    )

    hero_text_fa = models.TextField(
        blank=True
    )

    hero_text_en = models.TextField(
        blank=True
    )

    hero_about_button_fa = models.CharField(
        max_length=100,
        blank=True
    )

    hero_about_button_en = models.CharField(
        max_length=100,
        blank=True
    )

    hero_join_button_fa = models.CharField(
        max_length=100,
        blank=True
    )

    hero_join_button_en = models.CharField(
        max_length=100,
        blank=True
    )


    # =====================================================
    # HERO VISUAL
    # =====================================================

    hero_image = models.ImageField(
        upload_to="site/hero/",
        blank=True,
        null=True
    )

    hero_image_alt_fa = models.CharField(
        max_length=200,
        blank=True
    )

    hero_image_alt_en = models.CharField(
        max_length=200,
        blank=True
    )

    hero_badge_title = models.CharField(
        max_length=100,
        default="AWMJA"
    )

    hero_badge_text_fa = models.CharField(
        max_length=100,
        blank=True
    )

    hero_badge_text_en = models.CharField(
        max_length=100,
        blank=True
    )


    # =====================================================
    # CONTACT
    # =====================================================

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=50,
        blank=True
    )

    address_fa = models.CharField(
        max_length=255,
        blank=True
    )

    address_en = models.CharField(
        max_length=255,
        blank=True
    )


    # =====================================================
    # SOCIAL MEDIA
    # =====================================================

    facebook = models.URLField(
        blank=True
    )

    instagram = models.URLField(
        blank=True
    )

    linkedin = models.URLField(
        blank=True
    )


    # =====================================================
    # SYSTEM
    # =====================================================

    updated_at = models.DateTimeField(
        auto_now=True
    )


    class Meta:

        verbose_name = "تنظیمات سایت"

        verbose_name_plural = "تنظیمات سایت"


    def __str__(self):

        return self.site_name_fa





class ActivityPageSettings(models.Model):
    # =====================================================
    # ACTIVITIES HERO
    # =====================================================

    hero_kicker_fa = models.CharField(
        max_length=200,
        blank=True
    )

    hero_kicker_en = models.CharField(
        max_length=200,
        blank=True
    )

    hero_title_fa = models.CharField(
        max_length=300,
        blank=True
    )

    hero_title_en = models.CharField(
        max_length=300,
        blank=True
    )

    hero_lead_fa = models.TextField(
        blank=True
    )

    hero_lead_en = models.TextField(
        blank=True
    )

    hero_text_fa = models.TextField(
        blank=True
    )

    hero_text_en = models.TextField(
        blank=True
    )

    hero_image = models.ImageField(
        upload_to="activities/hero/",
        blank=True,
        null=True
    )

    hero_image_alt_fa = models.CharField(
        max_length=255,
        blank=True
    )

    hero_image_alt_en = models.CharField(
        max_length=255,
        blank=True
    )

    hero_quote_fa = models.TextField(
        blank=True
    )

    hero_quote_en = models.TextField(
        blank=True
    )

    hero_stat_number = models.CharField(
        max_length=20,
        blank=True
    )

    hero_stat_label_fa = models.CharField(
        max_length=200,
        blank=True
    )

    hero_stat_label_en = models.CharField(
        max_length=200,
        blank=True
    )

    # =====================================================
    # SYSTEM
    # =====================================================

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "تنظیمات Hero فعالیت‌ها"
        verbose_name_plural = "تنظیمات Hero فعالیت‌ها"

    def __str__(self):
        return "تنظیمات Hero فعالیت‌ها" 
    
    
    
    
    
##################################################
class Activity(models.Model):

    # =====================================================
    # BASIC INFORMATION
    # =====================================================

    number = models.PositiveIntegerField(
        default=1,
        verbose_name="شماره فعالیت"
    )

    category_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="دسته‌بندی فارسی"
    )

    category_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="دسته‌بندی انگلیسی"
    )

    title_fa = models.CharField(
        max_length=300,
        verbose_name="عنوان فارسی"
    )

    title_en = models.CharField(
        max_length=300,
        verbose_name="عنوان انگلیسی"
    )

    description_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )

    description_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )


    # =====================================================
    # ICON
    # =====================================================

    icon = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="آیکون"
    )

    icon_style = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="استایل آیکون"
    )


    # =====================================================
    # IMAGE
    # =====================================================

    image = models.ImageField(
        upload_to="activities/",
        blank=True,
        null=True,
        verbose_name="تصویر فعالیت"
    )

    image_alt_fa = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر فارسی"
    )

    image_alt_en = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر انگلیسی"
    )


    # =====================================================
    # LINK
    # =====================================================

    link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="لینک فعالیت"
    )


    # =====================================================
    # STATUS & ORDER
    # =====================================================

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )
    is_featured = models.BooleanField(
    default=False,
    verbose_name="نمایش در فعالیت‌های منتخب"
)

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )


    # =====================================================
    # SYSTEM
    # =====================================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    class Meta:

        verbose_name = "فعالیت"
        verbose_name_plural = "فعالیت‌ها"

        ordering = [
            "order",
            "number",
        ]


    def __str__(self):

        return self.title_fa
    
    #activity impact
class ActivityImpact(models.Model):

    # =====================================================
    # CONTENT
    # =====================================================

    number = models.PositiveIntegerField(
        default=1,
        verbose_name="شماره"
    )

    value = models.PositiveIntegerField(
        default=0,
        verbose_name="عدد"
    )

    label_fa = models.CharField(
        max_length=255,
        verbose_name="عنوان فارسی"
    )

    label_en = models.CharField(
        max_length=255,
        verbose_name="عنوان انگلیسی"
    )

    # =====================================================
    # STATUS & ORDER
    # =====================================================

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    # =====================================================
    # SYSTEM
    # =====================================================

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name = "آمار اثرگذاری فعالیت‌ها"
        verbose_name_plural = "آمار اثرگذاری فعالیت‌ها"

        ordering = [
            "order",
            "number",
        ]

    def __str__(self):
        return self.label_fa


# =====================================================
# ACTIVITY IMPACT SETTINGS
# =====================================================
class ActivityImpactSettings(models.Model):

    # =====================================================
    # IMPACT SECTION CONTENT
    # =====================================================

    kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب فارسی"
    )

    kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب انگلیسی"
    )

    title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان فارسی"
    )

    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )

    text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )

    button_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه فارسی"
    )

    button_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه انگلیسی"
    )

    # =====================================================
    # META
    # =====================================================

    class Meta:
        verbose_name = "تنظیمات بخش اثرگذاری فعالیت‌ها"
        verbose_name_plural = "تنظیمات بخش اثرگذاری فعالیت‌ها"

    def __str__(self):
        return "تنظیمات بخش اثرگذاری فعالیت‌ها"


# =====================================================
# ACTIVITY CTA SETTINGS
# =====================================================
class ActivityCTASettings(models.Model):

    # =====================================================
    # CTA CONTENT
    # =====================================================

    kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب فارسی"
    )

    kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب انگلیسی"
    )

    title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان فارسی"
    )

    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )

    text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )

    # =====================================================
    # BUTTONS
    # =====================================================

    primary_button_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="دکمه اصلی فارسی"
    )

    primary_button_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="دکمه اصلی انگلیسی"
    )

    secondary_button_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="دکمه دوم فارسی"
    )

    secondary_button_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="دکمه دوم انگلیسی"
    )

    # =====================================================
    # LINKS
    # =====================================================

    primary_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="لینک دکمه اصلی"
    )

    secondary_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="لینک دکمه دوم"
    )

    # =====================================================
    # SYSTEM
    # =====================================================

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "تنظیمات CTA فعالیت‌ها"
        verbose_name_plural = "تنظیمات CTA فعالیت‌ها"

    def __str__(self):
        return "تنظیمات CTA فعالیت‌ها"


# =====================================================
# ACTIVITY STORY
# =====================================================
class ActivityStory(models.Model):

    # =====================================================
    # BASIC INFORMATION
    # =====================================================

    number = models.PositiveIntegerField(
        default=1,
        verbose_name="شماره روایت"
    )

    category_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="دسته‌بندی فارسی"
    )

    category_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="دسته‌بندی انگلیسی"
    )

    title_fa = models.CharField(
        max_length=300,
        verbose_name="عنوان فارسی"
    )

    title_en = models.CharField(
        max_length=300,
        verbose_name="عنوان انگلیسی"
    )

    description_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )

    description_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )

    # =====================================================
    # IMAGE
    # =====================================================

    image = models.ImageField(
        upload_to="activities/stories/",
        blank=True,
        null=True,
        verbose_name="تصویر روایت"
    )

    image_alt_fa = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر فارسی"
    )

    image_alt_en = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر انگلیسی"
    )

    # =====================================================
    # LINK
    # =====================================================

    link = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="لینک روایت"
    )

    # =====================================================
    # STATUS & ORDER
    # =====================================================

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    # =====================================================
    # SYSTEM
    # =====================================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    # =====================================================
    # META
    # =====================================================

    class Meta:
        verbose_name = "روایت فعالیت"
        verbose_name_plural = "روایت‌های فعالیت"

        ordering = [
            "order",
            "number",
        ]

    def __str__(self):
        return self.title_fa
 # =====================================================
# ABOUT SETTINGS
# =====================================================

class AboutSettings(models.Model):

    # =========================
    # HOME / ABOUT PREVIEW
    # =========================

    preview_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب پیش‌نمایش فارسی"
    )

    preview_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب پیش‌نمایش انگلیسی"
    )

    preview_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان پیش‌نمایش فارسی"
    )

    preview_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان پیش‌نمایش انگلیسی"
    )

    preview_text_fa = models.TextField(
        blank=True,
        verbose_name="متن پیش‌نمایش فارسی"
    )

    preview_text_en = models.TextField(
        blank=True,
        verbose_name="متن پیش‌نمایش انگلیسی"
    )

    preview_button_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه پیش‌نمایش فارسی"
    )

    preview_button_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه پیش‌نمایش انگلیسی"
    )

    preview_link = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="لینک پیش‌نمایش"
    )

    preview_image = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True,
        verbose_name="تصویر پیش‌نمایش"
    )

    preview_image_alt_fa = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر فارسی"
    )

    preview_image_alt_en = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر انگلیسی"
    )

    foundation_year = models.PositiveIntegerField(
        default=2022,
        verbose_name="سال تأسیس"
    )

    foundation_label_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان سال تأسیس فارسی"
    )

    foundation_label_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان سال تأسیس انگلیسی"
    )

    # =========================
    # ABOUT HERO
    # =========================

    hero_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب Hero فارسی"
    )

    hero_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب Hero انگلیسی"
    )

    hero_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان Hero فارسی"
    )

    hero_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان Hero انگلیسی"
    )

    hero_text_fa = models.TextField(
        blank=True,
        verbose_name="متن Hero فارسی"
    )

    hero_text_en = models.TextField(
        blank=True,
        verbose_name="متن Hero انگلیسی"
    )

    hero_image = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True,
        verbose_name="تصویر Hero"
    )

    hero_image_alt_fa = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین Hero فارسی"
    )

    hero_image_alt_en = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین Hero انگلیسی"
    )

    hero_badge_top_fa = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="متن بالای نشان Hero فارسی"
    )

    hero_badge_top_en = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="متن بالای نشان Hero انگلیسی"
    )

    hero_badge_bottom_fa = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="متن پایین نشان Hero فارسی"
    )

    hero_badge_bottom_en = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="متن پایین نشان Hero انگلیسی"
    )

    # =========================
    # META
    # =========================

    class Meta:
        verbose_name = "تنظیمات درباره ما"
        verbose_name_plural = "تنظیمات درباره ما"

    def __str__(self):
        return "تنظیمات درباره ما"

#about hilihght
class AboutHighlight(models.Model):
    title_fa = models.CharField(
        max_length=100,
        verbose_name="عنوان فارسی"
    )

    title_en = models.CharField(
        max_length=100,
        verbose_name="عنوان انگلیسی"
    )

    description_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )

    description_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="آیکون"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    class Meta:
        verbose_name = "ویژگی درباره ما"
        verbose_name_plural = "ویژگی‌های درباره ما"
        ordering = ["order"]

    def __str__(self):
        return self.title_fa
    
class AboutIntroduction(models.Model):
    kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب فارسی"
    )
    kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب انگلیسی"
    )

    title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان فارسی"
    )
    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    intro_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی داخل بخش"
    )

    lead_fa = models.TextField(
        blank=True,
        verbose_name="متن اصلی فارسی"
    )
    lead_en = models.TextField(
        blank=True,
        verbose_name="متن اصلی انگلیسی"
    )

    text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )
    text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )

    highlight_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="نام کوتاه"
    )
    highlight_text = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="متن برجسته"
    )

    class Meta:
        verbose_name = "معرفی درباره ما"
        verbose_name_plural = "معرفی درباره ما"

    def __str__(self):
        return self.title_fa or "معرفی درباره ما"

#About story
class AboutStory(models.Model):
    number = models.PositiveIntegerField(
        default=1,
        verbose_name="شماره روایت"
    )

    date_main = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="تاریخ اصلی"
    )

    date_sub = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="تاریخ فرعی"
    )

    title_fa = models.CharField(
        max_length=300,
        verbose_name="عنوان فارسی"
    )

    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    description_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )

    description_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )

    image = models.ImageField(
        upload_to="about/stories/",
        blank=True,
        null=True,
        verbose_name="تصویر روایت"
    )

    image_alt_fa = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر فارسی"
    )

    image_alt_en = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر انگلیسی"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "روایت درباره ما"
        verbose_name_plural = "روایت‌های درباره ما"
        ordering = ["order", "number"]

    def __str__(self):
        return self.title_fa
    
    
class AboutMissionVision(models.Model):
    kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب فارسی"
    )

    kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب انگلیسی"
    )

    title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان فارسی"
    )

    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    intro_fa = models.TextField(
        blank=True,
        verbose_name="مقدمه فارسی"
    )

    intro_en = models.TextField(
        blank=True,
        verbose_name="مقدمه انگلیسی"
    )

    mission_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="شماره مأموریت"
    )

    mission_label_fa = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="برچسب مأموریت فارسی"
    )

    mission_label_en = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="برچسب مأموریت انگلیسی"
    )

    mission_icon = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="آیکون مأموریت"
    )

    mission_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان مأموریت فارسی"
    )

    mission_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان مأموریت انگلیسی"
    )

    mission_lead_fa = models.TextField(
        blank=True,
        verbose_name="متن اصلی مأموریت فارسی"
    )

    mission_lead_en = models.TextField(
        blank=True,
        verbose_name="متن اصلی مأموریت انگلیسی"
    )

    mission_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات مأموریت فارسی"
    )

    mission_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات مأموریت انگلیسی"
    )

    mission_footer_1 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="پایین مأموریت ۱"
    )

    mission_footer_2 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="پایین مأموریت ۲"
    )

    mission_footer_3 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="پایین مأموریت ۳"
    )

    vision_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="شماره چشم‌انداز"
    )

    vision_label_fa = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="برچسب چشم‌انداز فارسی"
    )

    vision_label_en = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="برچسب چشم‌انداز انگلیسی"
    )

    vision_icon = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="آیکون چشم‌انداز"
    )

    vision_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان چشم‌انداز فارسی"
    )

    vision_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان چشم‌انداز انگلیسی"
    )

    vision_lead_fa = models.TextField(
        blank=True,
        verbose_name="متن اصلی چشم‌انداز فارسی"
    )

    vision_lead_en = models.TextField(
        blank=True,
        verbose_name="متن اصلی چشم‌انداز انگلیسی"
    )

    vision_footer_1 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="پایین چشم‌انداز ۱"
    )

    vision_footer_2 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="پایین چشم‌انداز ۲"
    )

    vision_footer_3 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="پایین چشم‌انداز ۳"
    )

    class Meta:
         verbose_name = "ماموریت و چشم‌انداز — About"
    verbose_name_plural = "ماموریت و چشم‌انداز — About"
    def __str__(self):
        return self.title_fa or "مأموریت و چشم‌انداز"
    
class AboutVisionPoint(models.Model):
    number = models.PositiveIntegerField(
        default=1,
        verbose_name="شماره"
    )

    title_fa = models.CharField(
        max_length=300,
        verbose_name="عنوان فارسی"
    )

    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    class Meta:
        verbose_name = "مورد چشم‌انداز — About"
        verbose_name_plural = "موارد چشم‌انداز — About"
        ordering = ["order", "number"]

    def __str__(self):
        return self.title_fa

class AboutGoalsSettings(models.Model):
    kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب فارسی"
    )

    kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب انگلیسی"
    )

    title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان فارسی"
    )

    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    intro_fa = models.TextField(
        blank=True,
        verbose_name="مقدمه فارسی"
    )

    intro_en = models.TextField(
        blank=True,
        verbose_name="مقدمه انگلیسی"
    )

    closing_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="نام پایانی"
    )

    closing_text_fa = models.TextField(
        blank=True,
        verbose_name="متن پایانی فارسی"
    )

    closing_text_en = models.TextField(
        blank=True,
        verbose_name="متن پایانی انگلیسی"
    )

    class Meta:
        verbose_name = "تنظیمات اهداف — About"
        verbose_name_plural = "تنظیمات اهداف — About"

    def __str__(self):
        return self.title_fa or "تنظیمات اهداف — About"
    
class AboutGoal(models.Model):
    number = models.PositiveIntegerField(
        default=1,
        verbose_name="شماره هدف"
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="آیکون"
    )

    title_fa = models.CharField(
        max_length=300,
        verbose_name="عنوان فارسی"
    )

    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    description_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )

    description_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    class Meta:
        verbose_name = "هدف — About"
        verbose_name_plural = "اهداف — About"
        ordering = ["order", "number"]

    def __str__(self):
        return self.title_fa
# home impact ###################################################
class HomeImpactSettings(models.Model):
    kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب فارسی"
    )
    kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب انگلیسی"
    )

    title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان فارسی"
    )
    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )
    text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )

    class Meta:
        verbose_name = "تنظیمات اثرگذاری صفحه اصلی"
        verbose_name_plural = "تنظیمات اثرگذاری صفحه اصلی"

    def __str__(self):
        return self.title_fa or "تنظیمات اثرگذاری صفحه اصلی"


class HomeImpact(models.Model):
    number = models.CharField(
        max_length=50,
        verbose_name="عدد"
    )

    label_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان فارسی"
    )
    label_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    class Meta:
        verbose_name = "آمار اثرگذاری صفحه اصلی"
        verbose_name_plural = "آمارهای اثرگذاری صفحه اصلی"
        ordering = ["order"]

    def __str__(self):
        return f"{self.number} - {self.label_fa}"
    
#NEWS SECTION
class NewsPageSettings(models.Model):
    # NEWS HERO
    hero_kicker_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="برچسب Hero فارسی"
    )
    hero_kicker_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="برچسب Hero انگلیسی"
    )

    hero_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان Hero فارسی"
    )
    hero_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان Hero انگلیسی"
    )

    hero_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات Hero فارسی"
    )
    hero_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات Hero انگلیسی"
    )

    # FEATURED SECTION
    featured_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب خبر ویژه فارسی"
    )
    featured_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب خبر ویژه انگلیسی"
    )

    featured_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان خبر ویژه فارسی"
    )
    featured_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان خبر ویژه انگلیسی"
    )

    # LATEST NEWS
    latest_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب آخرین اخبار فارسی"
    )
    latest_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب آخرین اخبار انگلیسی"
    )

    latest_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان آخرین اخبار فارسی"
    )
    latest_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان آخرین اخبار انگلیسی"
    )

    latest_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات آخرین اخبار فارسی"
    )
    latest_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات آخرین اخبار انگلیسی"
    )

    # MEDIA & SOURCES
    media_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب رسانه و منابع فارسی"
    )
    media_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب رسانه و منابع انگلیسی"
    )

    media_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان رسانه و منابع فارسی"
    )
    media_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان رسانه و منابع انگلیسی"
    )

    media_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات رسانه و منابع فارسی"
    )
    media_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات رسانه و منابع انگلیسی"
    )

    media_note_title_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان یادداشت رسانه فارسی"
    )
    media_note_title_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان یادداشت رسانه انگلیسی"
    )

    media_note_text_fa = models.TextField(
        blank=True,
        verbose_name="متن یادداشت رسانه فارسی"
    )
    media_note_text_en = models.TextField(
        blank=True,
        verbose_name="متن یادداشت رسانه انگلیسی"
    )

    # NEWS ARCHIVE
    archive_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب آرشیو فارسی"
    )
    archive_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب آرشیو انگلیسی"
    )

    archive_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان آرشیو فارسی"
    )
    archive_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان آرشیو انگلیسی"
    )

    archive_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات آرشیو فارسی"
    )
    archive_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات آرشیو انگلیسی"
    )

    archive_button_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="دکمه آرشیو فارسی"
    )
    archive_button_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="دکمه آرشیو انگلیسی"
    )

    archive_link = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="لینک آرشیو"
    )

    class Meta:
        verbose_name = "تنظیمات اخبار"
        verbose_name_plural = "تنظیمات اخبار"

    def __str__(self):
        return self.hero_title_fa or "تنظیمات اخبار"
# NEWS SECTION END
class News(models.Model):
    CATEGORY_CHOICES = (
        ("statement", "بیانیه‌ها"),
        ("activity", "فعالیت‌ها"),
        ("international", "فعالیت بین‌المللی"),
        ("women-rights", "حقوق زنان"),
    )

    title_fa = models.CharField(
        max_length=300,
        verbose_name="عنوان فارسی"
    )
    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    excerpt_fa = models.TextField(
        blank=True,
        verbose_name="خلاصه فارسی"
    )
    excerpt_en = models.TextField(
        blank=True,
        verbose_name="خلاصه انگلیسی"
    )

    content_fa = models.TextField(
        blank=True,
        verbose_name="محتوای کامل فارسی"
    )
    content_en = models.TextField(
        blank=True,
        verbose_name="محتوای کامل انگلیسی"
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="statement",
        verbose_name="دسته‌بندی"
    )

    category_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان دسته‌بندی فارسی"
    )
    category_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان دسته‌بندی انگلیسی"
    )

    image = models.ImageField(
        upload_to="news/",
        blank=True,
        null=True,
        verbose_name="تصویر خبر"
    )

    image_alt_fa = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر فارسی"
    )
    image_alt_en = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر انگلیسی"
    )

    published_at = models.DateField(
        verbose_name="تاریخ انتشار"
    )

    source = models.CharField(
        max_length=200,
        default="AWMJA",
        verbose_name="منبع"
    )

    source_url = models.URLField(
        blank=True,
        verbose_name="لینک منبع"
    )
    external_url = models.URLField(
    blank=True,
    verbose_name="لینک ادامه مطلب"
)
    slug = models.SlugField(
        max_length=300,
        unique=True,
        verbose_name="Slug"
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name="خبر ویژه"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "اخبار"
        ordering = ["-published_at", "order"]

    def __str__(self):
        return self.title_fa
    
# EVENT SECTION
class Event(models.Model):
    STATUS_CHOICES = (
        ("upcoming", "رویداد پیش‌رو"),
        ("past", "رویداد گذشته"),
    )

    CATEGORY_CHOICES = (
        ("international", "بین‌المللی"),
        ("advocacy", "دادخواهی"),
        ("human-rights", "حقوق بشر"),
        ("meeting", "نشست"),
        ("conference", "کنفرانس"),
        ("other", "سایر"),
    )

    title_fa = models.CharField(
        max_length=300,
        verbose_name="عنوان فارسی"
    )

    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    description_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )

    description_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="other",
        verbose_name="دسته‌بندی"
    )

    category_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان دسته‌بندی فارسی"
    )

    category_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان دسته‌بندی انگلیسی"
    )

    image = models.ImageField(
        upload_to="events/",
        blank=True,
        null=True,
        verbose_name="تصویر رویداد"
    )

    image_alt_fa = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر فارسی"
    )

    image_alt_en = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر انگلیسی"
    )

    event_date = models.DateField(
        verbose_name="تاریخ رویداد"
    )

    location_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="مکان فارسی"
    )

    location_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="مکان انگلیسی"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="upcoming",
        verbose_name="وضعیت رویداد"
    )

    external_url = models.URLField(
        blank=True,
        verbose_name="لینک جزئیات"
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name="رویداد ویژه"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "رویداد"
        verbose_name_plural = "رویدادها"
        ordering = ["-event_date", "order"]

    def __str__(self):
        return self.title_fa
#SECTION GALLERY
class GalleryAlbum(models.Model):
    CATEGORY_CHOICES = (
        ("advocacy", "دادخواهی"),
        ("meetings", "نشست‌ها"),
        ("international", "بین‌المللی"),
        ("empowerment", "توانمندسازی"),
        ("events", "رویدادها"),
        ("other", "سایر"),
    )

    title_fa = models.CharField(
        max_length=300,
        verbose_name="عنوان فارسی"
    )

    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    description_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )

    description_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="other",
        verbose_name="دسته‌بندی"
    )

    category_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان دسته‌بندی فارسی"
    )

    category_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان دسته‌بندی انگلیسی"
    )

    cover_image = models.ImageField(
        upload_to="gallery/covers/",
        blank=True,
        null=True,
        verbose_name="تصویر روی جلد آلبوم"
    )

    cover_alt_fa = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین جلد فارسی"
    )

    cover_alt_en = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین جلد انگلیسی"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "آلبوم گالری"
        verbose_name_plural = "آلبوم‌های گالری"
        ordering = ["order", "id"]

    def __str__(self):
        return self.title_fa


class GalleryMedia(models.Model):
    MEDIA_TYPE_CHOICES = (
        ("image", "تصویر"),
        ("video", "ویدیو"),
    )

    album = models.ForeignKey(
        GalleryAlbum,
        on_delete=models.CASCADE,
        related_name="media",
        verbose_name="آلبوم"
    )

    media_type = models.CharField(
        max_length=20,
        choices=MEDIA_TYPE_CHOICES,
        default="image",
        verbose_name="نوع رسانه"
    )

    image = models.ImageField(
        upload_to="gallery/images/",
        blank=True,
        null=True,
        verbose_name="تصویر"
    )

    video = models.FileField(
        upload_to="gallery/videos/",
        blank=True,
        null=True,
        verbose_name="ویدیو"
    )

    title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان فارسی"
    )

    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    description_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )

    description_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )

    image_alt_fa = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر فارسی"
    )

    image_alt_en = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر انگلیسی"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "رسانه گالری"
        verbose_name_plural = "رسانه‌های گالری"
        ordering = ["order", "id"]

    def __str__(self):
        return self.title_fa or f"رسانه آلبوم {self.album.title_fa}"
    
#MISSIONS SECTION
# =========================================================
# MISSION & VISION
# =========================================================

class MissionVisionSettings(models.Model):

    # -----------------------------------------------------
    # HERO
    # -----------------------------------------------------

    hero_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب Hero فارسی"
    )

    hero_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب Hero انگلیسی"
    )

    hero_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان Hero فارسی"
    )

    hero_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان Hero انگلیسی"
    )

    hero_highlight_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته Hero فارسی"
    )

    hero_highlight_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته Hero انگلیسی"
    )

    hero_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات Hero فارسی"
    )

    hero_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات Hero انگلیسی"
    )


    # -----------------------------------------------------
    # MISSION
    # -----------------------------------------------------

    mission_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب مأموریت فارسی"
    )

    mission_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب مأموریت انگلیسی"
    )

    mission_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان مأموریت فارسی"
    )

    mission_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان مأموریت انگلیسی"
    )

    mission_lead_fa = models.TextField(
        blank=True,
        verbose_name="متن اصلی مأموریت فارسی"
    )

    mission_lead_en = models.TextField(
        blank=True,
        verbose_name="متن اصلی مأموریت انگلیسی"
    )

    mission_text_fa = models.TextField(
        blank=True,
        verbose_name="متن تکمیلی مأموریت فارسی"
    )

    mission_text_en = models.TextField(
        blank=True,
        verbose_name="متن تکمیلی مأموریت انگلیسی"
    )

    mission_text_2_fa = models.TextField(
        blank=True,
        verbose_name="متن دوم مأموریت فارسی"
    )

    mission_text_2_en = models.TextField(
        blank=True,
        verbose_name="متن دوم مأموریت انگلیسی"
    )

    mission_image = models.ImageField(
        upload_to="mission/",
        blank=True,
        null=True,
        verbose_name="تصویر مأموریت"
    )

    mission_image_alt_fa = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر مأموریت فارسی"
    )

    mission_image_alt_en = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر مأموریت انگلیسی"
    )

    mission_badge_title_fa = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="عنوان نشان مأموریت فارسی"
    )

    mission_badge_title_en = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="عنوان نشان مأموریت انگلیسی"
    )

    mission_badge_text_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن نشان مأموریت فارسی"
    )

    mission_badge_text_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن نشان مأموریت انگلیسی"
    )


    # -----------------------------------------------------
    # VISION
    # -----------------------------------------------------

    vision_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب چشم‌انداز فارسی"
    )

    vision_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب چشم‌انداز انگلیسی"
    )

    vision_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان چشم‌انداز فارسی"
    )

    vision_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان چشم‌انداز انگلیسی"
    )

    vision_lead_fa = models.TextField(
        blank=True,
        verbose_name="متن اصلی چشم‌انداز فارسی"
    )

    vision_lead_en = models.TextField(
        blank=True,
        verbose_name="متن اصلی چشم‌انداز انگلیسی"
    )

    vision_text_fa = models.TextField(
        blank=True,
        verbose_name="متن تکمیلی چشم‌انداز فارسی"
    )

    vision_text_en = models.TextField(
        blank=True,
        verbose_name="متن تکمیلی چشم‌انداز انگلیسی"
    )

    vision_statement_fa = models.TextField(
        blank=True,
        verbose_name="بیانیه چشم‌انداز فارسی"
    )

    vision_statement_en = models.TextField(
        blank=True,
        verbose_name="بیانیه چشم‌انداز انگلیسی"
    )


    # -----------------------------------------------------
    # FINAL CTA
    # -----------------------------------------------------

    cta_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب CTA فارسی"
    )

    cta_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب CTA انگلیسی"
    )

    cta_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان CTA فارسی"
    )

    cta_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان CTA انگلیسی"
    )

    cta_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات CTA فارسی"
    )

    cta_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات CTA انگلیسی"
    )

    cta_button_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه همکاری فارسی"
    )

    cta_button_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه همکاری انگلیسی"
    )

    cta_button_2_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه دوم فارسی"
    )

    cta_button_2_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه دوم انگلیسی"
    )


    class Meta:
        verbose_name = "تنظیمات مأموریت و چشم‌انداز"
        verbose_name_plural = "تنظیمات مأموریت و چشم‌انداز"

    def __str__(self):
        return self.hero_title_fa or "تنظیمات مأموریت و چشم‌انداز"


# =========================================================
# MISSION POINTS
# =========================================================

class MissionPoint(models.Model):

    number = models.PositiveIntegerField(
        default=1,
        verbose_name="شماره"
    )

    title_fa = models.CharField(
        max_length=300,
        verbose_name="عنوان فارسی"
    )

    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    description_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )

    description_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    class Meta:
        verbose_name = "مورد مأموریت"
        verbose_name_plural = "موارد مأموریت"
        ordering = ["order", "number"]

    def __str__(self):
        return self.title_fa


# =========================================================
# CORE VALUES
# =========================================================

class CoreValue(models.Model):

    number = models.PositiveIntegerField(
        default=1,
        verbose_name="شماره"
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="آیکون"
    )

    title_fa = models.CharField(
        max_length=300,
        verbose_name="عنوان فارسی"
    )

    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    description_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )

    description_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    class Meta:
        verbose_name = "ارزش اصلی"
        verbose_name_plural = "ارزش‌های اصلی"
        ordering = ["order", "number"]

    def __str__(self):
        return self.title_fa


# =========================================================
# APPROACH STEPS
# =========================================================

class ApproachStep(models.Model):

    number = models.PositiveIntegerField(
        default=1,
        verbose_name="شماره مرحله"
    )

    title_fa = models.CharField(
        max_length=300,
        verbose_name="عنوان فارسی"
    )

    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    description_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )

    description_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    class Meta:
        verbose_name = "مرحله رویکرد"
        verbose_name_plural = "مراحل رویکرد"
        ordering = ["order", "number"]

    def __str__(self):
        return self.title_fa

#ACHIEVMENT 
class AchievementPageSettings(models.Model):
    # HERO
    hero_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب Hero فارسی"
    )
    hero_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب Hero انگلیسی"
    )
    hero_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان Hero فارسی"
    )
    hero_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان Hero انگلیسی"
    )
    hero_highlight_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته Hero فارسی"
    )
    hero_highlight_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته Hero انگلیسی"
    )
    hero_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات Hero فارسی"
    )
    hero_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات Hero انگلیسی"
    )
    hero_button_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه Hero فارسی"
    )
    hero_button_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه Hero انگلیسی"
    )
    hero_button_2_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه دوم Hero فارسی"
    )
    hero_button_2_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه دوم Hero انگلیسی"
    )

    # IMPACT INTRO
    intro_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب معرفی اثرگذاری فارسی"
    )
    intro_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب معرفی اثرگذاری انگلیسی"
    )
    intro_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان معرفی اثرگذاری فارسی"
    )
    intro_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان معرفی اثرگذاری انگلیسی"
    )
    intro_highlight_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته معرفی فارسی"
    )
    intro_highlight_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته معرفی انگلیسی"
    )
    intro_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات معرفی فارسی"
    )
    intro_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات معرفی انگلیسی"
    )

    # KEY ACHIEVEMENTS
    achievements_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب دستاوردهای شاخص فارسی"
    )
    achievements_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب دستاوردهای شاخص انگلیسی"
    )
    achievements_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان دستاوردهای شاخص فارسی"
    )
    achievements_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان دستاوردهای شاخص انگلیسی"
    )
    achievements_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات دستاوردهای شاخص فارسی"
    )
    achievements_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات دستاوردهای شاخص انگلیسی"
    )

    # TIMELINE
    timeline_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب مسیر فعالیت فارسی"
    )
    timeline_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب مسیر فعالیت انگلیسی"
    )
    timeline_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان مسیر فعالیت فارسی"
    )
    timeline_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان مسیر فعالیت انگلیسی"
    )
    timeline_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات مسیر فعالیت فارسی"
    )
    timeline_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات مسیر فعالیت انگلیسی"
    )

    # MEDIA
    media_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب رسانه فارسی"
    )
    media_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب رسانه انگلیسی"
    )
    media_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان رسانه فارسی"
    )
    media_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان رسانه انگلیسی"
    )
    media_highlight_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته رسانه فارسی"
    )
    media_highlight_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته رسانه انگلیسی"
    )
    media_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات رسانه فارسی"
    )
    media_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات رسانه انگلیسی"
    )

    # EVIDENCE
    evidence_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب مستندات فارسی"
    )
    evidence_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب مستندات انگلیسی"
    )
    evidence_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان مستندات فارسی"
    )
    evidence_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان مستندات انگلیسی"
    )
    evidence_highlight_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته مستندات فارسی"
    )
    evidence_highlight_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته مستندات انگلیسی"
    )
    evidence_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات مستندات فارسی"
    )
    evidence_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات مستندات انگلیسی"
    )

    # FINAL CTA
    cta_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب CTA فارسی"
    )
    cta_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب CTA انگلیسی"
    )
    cta_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان CTA فارسی"
    )
    cta_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان CTA انگلیسی"
    )
    cta_highlight_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته CTA فارسی"
    )
    cta_highlight_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته CTA انگلیسی"
    )
    cta_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات CTA فارسی"
    )
    cta_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات CTA انگلیسی"
    )
    cta_button_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه CTA فارسی"
    )
    cta_button_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه CTA انگلیسی"
    )

    class Meta:
        verbose_name = "تنظیمات صفحه دستاوردها"
        verbose_name_plural = "تنظیمات صفحه دستاوردها"

    def __str__(self):
        return self.hero_title_fa or "تنظیمات صفحه دستاوردها"


class AchievementImpact(models.Model):
    number = models.CharField(
        max_length=50,
        verbose_name="عدد"
    )
    label_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان فارسی"
    )
    label_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )
    suffix = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="پسوند عدد"
    )
    stat_key = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="شناسه آماری"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    class Meta:
        verbose_name = "آمار دستاوردها"
        verbose_name_plural = "آمارهای دستاوردها"
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.number} - {self.label_fa}"


class Achievement(models.Model):
    CATEGORY_CHOICES = (
        ("advocacy", "دادخواهی"),
        ("empowerment", "توانمندسازی"),
        ("international", "بین‌المللی"),
        ("media", "رسانه"),
        ("human-rights", "حقوق بشر"),
        ("cooperation", "همکاری"),
        ("other", "سایر"),
    )

    number = models.PositiveIntegerField(
        default=1,
        verbose_name="شماره دستاورد"
    )
    title_fa = models.CharField(
        max_length=300,
        verbose_name="عنوان فارسی"
    )
    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )
    description_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )
    description_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="other",
        verbose_name="دسته‌بندی"
    )
    category_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان دسته‌بندی فارسی"
    )
    category_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان دسته‌بندی انگلیسی"
    )
    icon = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="آیکون"
    )
    year = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="سال"
    )
    footer_label_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن پایین کارت فارسی"
    )
    footer_label_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن پایین کارت انگلیسی"
    )
    is_featured = models.BooleanField(
        default=False,
        verbose_name="دستاورد شاخص"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "دستاورد"
        verbose_name_plural = "دستاوردها"
        ordering = ["order", "number"]

    def __str__(self):
        return self.title_fa


class AchievementTimeline(models.Model):
    year = models.PositiveIntegerField(
        verbose_name="سال"
    )
    number = models.PositiveIntegerField(
        default=1,
        verbose_name="شماره"
    )
    title_fa = models.CharField(
        max_length=300,
        verbose_name="عنوان فارسی"
    )
    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )
    description_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )
    description_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    class Meta:
        verbose_name = "مسیر دستاورد"
        verbose_name_plural = "مسیر دستاوردها"
        ordering = ["order", "year"]

    def __str__(self):
        return f"{self.year} - {self.title_fa}"


class AchievementMedia(models.Model):
    source_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="منبع فارسی"
    )
    source_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="منبع انگلیسی"
    )
    title_fa = models.CharField(
        max_length=300,
        verbose_name="عنوان فارسی"
    )
    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )
    media_type = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="نوع رسانه"
    )
    url = models.URLField(
        blank=True,
        verbose_name="لینک رسانه"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    class Meta:
        verbose_name = "رسانه دستاورد"
        verbose_name_plural = "رسانه‌های دستاورد"
        ordering = ["order", "id"]

    def __str__(self):
        return self.title_fa   
#GOAL SECTION
class GoalPageSettings(models.Model):
    # HERO
    hero_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب Hero فارسی"
    )
    hero_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب Hero انگلیسی"
    )

    hero_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان Hero فارسی"
    )
    hero_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان Hero انگلیسی"
    )

    hero_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات Hero فارسی"
    )
    hero_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات Hero انگلیسی"
    )

    # MAIN GOALS
    goals_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب اهداف فارسی"
    )
    goals_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب اهداف انگلیسی"
    )

    goals_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان اهداف فارسی"
    )
    goals_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان اهداف انگلیسی"
    )

    goals_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات اهداف فارسی"
    )
    goals_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات اهداف انگلیسی"
    )

    # COMMITMENT
    commitment_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب تعهد فارسی"
    )
    commitment_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب تعهد انگلیسی"
    )

    commitment_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان تعهد فارسی"
    )
    commitment_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان تعهد انگلیسی"
    )

    commitment_highlight_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته تعهد فارسی"
    )
    commitment_highlight_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته تعهد انگلیسی"
    )

    commitment_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات تعهد فارسی"
    )
    commitment_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات تعهد انگلیسی"
    )

    # CTA
    cta_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب CTA فارسی"
    )
    cta_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب CTA انگلیسی"
    )

    cta_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان CTA فارسی"
    )
    cta_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان CTA انگلیسی"
    )

    cta_highlight_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته CTA فارسی"
    )
    cta_highlight_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته CTA انگلیسی"
    )

    cta_button_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه CTA فارسی"
    )
    cta_button_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه CTA انگلیسی"
    )

    class Meta:
        verbose_name = "تنظیمات صفحه اهداف"
        verbose_name_plural = "تنظیمات صفحه اهداف"

    def __str__(self):
        return self.hero_title_fa or "تنظیمات صفحه اهداف"


class Goal(models.Model):
    CATEGORY_CHOICES = (
        ("justice", "عدالت"),
        ("education", "آموزش"),
        ("equality", "برابری"),
        ("protection", "حفاظت"),
        ("advocacy", "دادخواهی"),
        ("empowerment", "توانمندسازی"),
        ("global-action", "اقدام جهانی"),
        ("participation", "مشارکت"),
        ("other", "سایر"),
    )

    number = models.PositiveIntegerField(
        default=1,
        verbose_name="شماره هدف"
    )

    title_fa = models.CharField(
        max_length=300,
        verbose_name="عنوان فارسی"
    )
    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    description_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات فارسی"
    )
    description_en = models.TextField(
        blank=True,
        verbose_name="توضیحات انگلیسی"
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="other",
        verbose_name="دسته‌بندی"
    )

    category_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان دسته‌بندی فارسی"
    )
    category_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان دسته‌بندی انگلیسی"
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="آیکون"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name="هدف شاخص"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "هدف"
        verbose_name_plural = "اهداف"
        ordering = ["order", "number"]

    def __str__(self):
        return self.title_fa
#leadership 
class Leader(models.Model):
    number = models.PositiveIntegerField(
        default=1,
        verbose_name="شماره عضو"
    )

    name_fa = models.CharField(
        max_length=200,
        verbose_name="نام فارسی"
    )

    name_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="نام انگلیسی"
    )

    role_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="سمت فارسی"
    )

    role_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="سمت انگلیسی"
    )

    kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب فارسی"
    )

    kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب انگلیسی"
    )

    bio_fa = models.TextField(
        blank=True,
        verbose_name="بیوگرافی فارسی"
    )

    bio_en = models.TextField(
        blank=True,
        verbose_name="بیوگرافی انگلیسی"
    )

    position_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان موقعیت فارسی"
    )

    position_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان موقعیت انگلیسی"
    )

    organization = models.CharField(
        max_length=100,
        default="AWMJA",
        blank=True,
        verbose_name="سازمان"
    )

    focus_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="حوزه فعالیت فارسی"
    )

    focus_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="حوزه فعالیت انگلیسی"
    )

    image = models.ImageField(
        upload_to="leaders/",
        blank=True,
        null=True,
        verbose_name="تصویر"
    )

    image_alt_fa = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر فارسی"
    )

    image_alt_en = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر انگلیسی"
    )

    facebook_url = models.URLField(
        blank=True,
        verbose_name="لینک Facebook"
    )

    twitter_url = models.URLField(
        blank=True,
        verbose_name="لینک Twitter"
    )

    linkedin_url = models.URLField(
        blank=True,
        verbose_name="لینک LinkedIn"
    )

    is_main = models.BooleanField(
        default=False,
        verbose_name="رهبر اصلی"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "عضو رهبری"
        verbose_name_plural = "اعضای رهبری"
        ordering = ["order", "number"]

    def __str__(self):
        return self.name_fa

#ARTICLES
class ArticlePageSettings(models.Model):
    hero_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب Hero فارسی"
    )
    hero_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب Hero انگلیسی"
    )

    hero_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان Hero فارسی"
    )
    hero_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان Hero انگلیسی"
    )

    hero_highlight_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="متن برجسته Hero فارسی"
    )
    hero_highlight_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="متن برجسته Hero انگلیسی"
    )

    hero_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات Hero فارسی"
    )
    hero_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات Hero انگلیسی"
    )

    featured_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب مقاله منتخب فارسی"
    )
    featured_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب مقاله منتخب انگلیسی"
    )

    featured_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان مقاله منتخب فارسی"
    )
    featured_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان مقاله منتخب انگلیسی"
    )

    featured_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات مقاله منتخب فارسی"
    )
    featured_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات مقاله منتخب انگلیسی"
    )

    articles_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب مقالات فارسی"
    )
    articles_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب مقالات انگلیسی"
    )

    articles_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان مقالات فارسی"
    )
    articles_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان مقالات انگلیسی"
    )

    articles_highlight_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته مقالات فارسی"
    )
    articles_highlight_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته مقالات انگلیسی"
    )

    articles_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات مقالات فارسی"
    )
    articles_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات مقالات انگلیسی"
    )

    cta_kicker_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب CTA فارسی"
    )
    cta_kicker_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب CTA انگلیسی"
    )

    cta_title_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان CTA فارسی"
    )
    cta_title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان CTA انگلیسی"
    )

    cta_highlight_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته CTA فارسی"
    )
    cta_highlight_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن برجسته CTA انگلیسی"
    )

    cta_text_fa = models.TextField(
        blank=True,
        verbose_name="توضیحات CTA فارسی"
    )
    cta_text_en = models.TextField(
        blank=True,
        verbose_name="توضیحات CTA انگلیسی"
    )

    cta_button_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه CTA فارسی"
    )
    cta_button_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن دکمه CTA انگلیسی"
    )

    class Meta:
        verbose_name = "تنظیمات صفحه مقالات"
        verbose_name_plural = "تنظیمات صفحه مقالات"

    def __str__(self):
        return self.hero_title_fa or "تنظیمات صفحه مقالات"


class Article(models.Model):

    CATEGORY_CHOICES = (
        ("women-rights", "حقوق زنان"),
        ("education", "آموزش"),
        ("social-justice", "عدالت اجتماعی"),
        ("society", "جامعه"),
        ("awareness", "آگاهی"),
        ("perspective", "دیدگاه"),
        ("other", "سایر"),
    )

    title_fa = models.CharField(
        max_length=300,
        verbose_name="عنوان فارسی"
    )

    title_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="عنوان انگلیسی"
    )

    excerpt_fa = models.TextField(
        blank=True,
        verbose_name="خلاصه فارسی"
    )

    excerpt_en = models.TextField(
        blank=True,
        verbose_name="خلاصه انگلیسی"
    )

    content_fa = models.TextField(
        blank=True,
        verbose_name="متن کامل فارسی"
    )

    content_en = models.TextField(
        blank=True,
        verbose_name="متن کامل انگلیسی"
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="other",
        verbose_name="دسته‌بندی"
    )

    category_fa = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان دسته‌بندی فارسی"
    )

    category_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان دسته‌بندی انگلیسی"
    )

    image = models.ImageField(
        upload_to="articles/",
        blank=True,
        null=True,
        verbose_name="تصویر مقاله"
    )

    image_alt_fa = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر فارسی"
    )

    image_alt_en = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین تصویر انگلیسی"
    )

    published_at = models.DateField(
        null=True,
        blank=True,
        verbose_name="تاریخ انتشار"
    )

    slug = models.SlugField(
        max_length=300,
        unique=True,
        verbose_name="Slug"
    )

    source_name = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="نام منبع"
    )

    source_url = models.URLField(
        blank=True,
        verbose_name="لینک منبع"
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name="مقاله منتخب"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ["-published_at", "order"]

    def __str__(self):
        return self.title_fa

# =========================================================
# CONTACT PAGE
# =========================================================

class ContactPageSettings(models.Model):

    # -----------------------------------------------------
    # HERO
    # -----------------------------------------------------

    hero_kicker_fa = models.CharField(max_length=200, blank=True)
    hero_kicker_en = models.CharField(max_length=200, blank=True)

    hero_title_fa = models.CharField(max_length=300, blank=True)
    hero_title_en = models.CharField(max_length=300, blank=True)

    hero_highlight_fa = models.CharField(max_length=300, blank=True)
    hero_highlight_en = models.CharField(max_length=300, blank=True)

    hero_text_fa = models.TextField(blank=True)
    hero_text_en = models.TextField(blank=True)


    # -----------------------------------------------------
    # CONTACT INFORMATION
    # -----------------------------------------------------

    email = models.EmailField(blank=True)

    whatsapp_number = models.CharField(max_length=50, blank=True)
    whatsapp_url = models.URLField(blank=True)

    phone_number = models.CharField(max_length=50, blank=True)
    phone_url = models.CharField(max_length=100, blank=True)

    location_fa = models.CharField(max_length=300, blank=True)
    location_en = models.CharField(max_length=300, blank=True)


    # -----------------------------------------------------
    # CONTACT FORM INTRO
    # -----------------------------------------------------

    form_kicker_fa = models.CharField(max_length=200, blank=True)
    form_kicker_en = models.CharField(max_length=200, blank=True)

    form_title_fa = models.CharField(max_length=300, blank=True)
    form_title_en = models.CharField(max_length=300, blank=True)

    form_highlight_fa = models.CharField(max_length=300, blank=True)
    form_highlight_en = models.CharField(max_length=300, blank=True)

    form_text_fa = models.TextField(blank=True)
    form_text_en = models.TextField(blank=True)

    privacy_note_fa = models.TextField(blank=True)
    privacy_note_en = models.TextField(blank=True)


    # -----------------------------------------------------
    # JOIN / SUPPORT
    # -----------------------------------------------------

    join_kicker_fa = models.CharField(max_length=200, blank=True)
    join_kicker_en = models.CharField(max_length=200, blank=True)

    join_title_fa = models.CharField(max_length=300, blank=True)
    join_title_en = models.CharField(max_length=300, blank=True)

    join_text_fa = models.TextField(blank=True)
    join_text_en = models.TextField(blank=True)

    join_button_fa = models.CharField(max_length=100, blank=True)
    join_button_en = models.CharField(max_length=100, blank=True)

    email_button_fa = models.CharField(max_length=100, blank=True)
    email_button_en = models.CharField(max_length=100, blank=True)


    # -----------------------------------------------------
    # META
    # -----------------------------------------------------

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Contact Page Settings"


# =========================================================
# CONTACT MESSAGES
# =========================================================

class ContactMessage(models.Model):

    SUBJECT_CHOICES = (
        ("membership", "عضویت در جنبش"),
        ("support", "حمایت از جنبش"),
        ("cooperation", "همکاری"),
        ("media", "همکاری رسانه‌ای"),
        ("general", "پرسش عمومی"),
        ("other", "سایر موارد"),
    )

    STATUS_CHOICES = (
        ("new", "جدید"),
        ("reviewing", "در حال بررسی"),
        ("replied", "پاسخ داده شد"),
        ("closed", "بسته شد"),
    )


    # -----------------------------------------------------
    # SENDER INFORMATION
    # -----------------------------------------------------

    name = models.CharField(max_length=200)

    email = models.EmailField()

    phone = models.CharField(
        max_length=50,
        blank=True
    )


    # -----------------------------------------------------
    # MESSAGE
    # -----------------------------------------------------

    subject = models.CharField(
        max_length=50,
        choices=SUBJECT_CHOICES
    )

    message = models.TextField()


    # -----------------------------------------------------
    # CONSENT
    # -----------------------------------------------------

    consent = models.BooleanField(default=False)


    # -----------------------------------------------------
    # MANAGEMENT
    # -----------------------------------------------------

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"


    def __str__(self):
        return f"{self.name} — {self.email}"
