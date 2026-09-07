
/* =========================================================
   AWMJA GALLERY
   Gallery / Albums / Images / Videos / Lightbox
   Django Ready Structure
   ========================================================= */

document.addEventListener("DOMContentLoaded", () => {

    /* =====================================================
       ELEMENTS
       ===================================================== */

    const albums = document.querySelectorAll(".gallery-album");
    const filters = document.querySelectorAll(".gallery-filter");

    const viewer = document.querySelector(".album-viewer");

    const viewerImage = document.querySelector(".viewer-image");
    const viewerVideo = document.querySelector(".viewer-video");

    const viewerTitle = document.querySelector(".viewer-title");
    const viewerDescription = document.querySelector(".viewer-description");
    const viewerCategory = document.querySelector(".viewer-category");
    const viewerCounter = document.querySelector(".viewer-counter");

    const closeButton = document.querySelector(".viewer-close");
    const previousButton = document.querySelector(".viewer-prev");
    const nextButton = document.querySelector(".viewer-next");


    /* =====================================================
       STATE
       ===================================================== */

    let currentAlbum = null;
    let currentMediaIndex = 0;

    let currentMedia = [];


    /* =====================================================
       SAFE CHECK
       ===================================================== */

    if (!viewer || !albums.length) {
        return;
    }


    /* =====================================================
       GET ALBUM MEDIA
       ===================================================== */

    function getAlbumMedia(album) {

        /*
         * هر آلبوم می‌تواند چند Media داشته باشد.
         *
         * مثال آینده برای Django:
         *
         * <div class="gallery-media"
         *      data-type="image"
         *      data-src="...">
         * </div>
         *
         * یا:
         *
         * data-type="video"
         * data-src="..."
         */

        const mediaElements = album.querySelectorAll(".gallery-media");

        const media = [];

        mediaElements.forEach((item) => {

            const type = item.dataset.type || "image";
            const src = item.dataset.src || "";

            const title =
                item.dataset.title ||
                album.dataset.title ||
                "";

            const description =
                item.dataset.description ||
                album.dataset.description ||
                "";

            if (!src) {
                return;
            }

            media.push({
                type,
                src,
                title,
                description
            });

        });

        return media;
    }


    /* =====================================================
       OPEN ALBUM
       ===================================================== */

    function openAlbum(album) {

        currentAlbum = album;
        currentMedia = getAlbumMedia(album);

        currentMediaIndex = 0;


        /*
         * اگر هنوز Media داخلی تعریف نشده باشد،
         * می‌توانیم از عکس Cover استفاده کنیم.
         */

        if (!currentMedia.length) {

            const cover = album.querySelector(".album-cover img");

            if (cover && cover.src) {

                currentMedia.push({
                    type: "image",
                    src: cover.src,
                    title: album.dataset.title || "",
                    description: album.dataset.description || ""
                });

            }

        }


        if (!currentMedia.length) {
            return;
        }


        viewer.classList.add("active");

        document.body.classList.add("gallery-viewer-open");

        document.body.style.overflow = "hidden";


        updateViewer();

    }


    /* =====================================================
       CLOSE ALBUM
       ===================================================== */

    function closeAlbum() {

        viewer.classList.remove("active");

        document.body.classList.remove("gallery-viewer-open");

        document.body.style.overflow = "";


        /*
         * توقف کامل ویدیو
         */

        if (viewerVideo) {

            viewerVideo.pause();

            viewerVideo.currentTime = 0;

            viewerVideo.removeAttribute("src");

            viewerVideo.load();

        }


        currentAlbum = null;
        currentMedia = [];
        currentMediaIndex = 0;

    }


    /* =====================================================
       UPDATE VIEWER
       ===================================================== */

    function updateViewer() {

        const media = currentMedia[currentMediaIndex];

        if (!media) {
            return;
        }


        /* -----------------------------------------------
           TITLE
           ----------------------------------------------- */

        if (viewerTitle) {
            viewerTitle.textContent =
                media.title ||
                currentAlbum?.dataset.title ||
                "AWMJA Gallery";
        }


        /* -----------------------------------------------
           DESCRIPTION
           ----------------------------------------------- */

        if (viewerDescription) {
            viewerDescription.textContent =
                media.description ||
                currentAlbum?.dataset.description ||
                "";
        }


        /* -----------------------------------------------
           CATEGORY
           ----------------------------------------------- */

        if (viewerCategory) {

            viewerCategory.textContent =
                currentAlbum?.dataset.category ||
                "GALLERY";

        }


        /* -----------------------------------------------
           COUNTER
           ----------------------------------------------- */

        if (viewerCounter) {

            viewerCounter.textContent =
                `${currentMediaIndex + 1} / ${currentMedia.length}`;

        }


        /* -----------------------------------------------
           HIDE BOTH
           ----------------------------------------------- */

        if (viewerImage) {
            viewerImage.classList.remove("active");
        }

        if (viewerVideo) {
            viewerVideo.classList.remove("active");
        }


        /* =================================================
           IMAGE
           ================================================= */

        if (media.type === "image") {

            if (!viewerImage) {
                return;
            }

            viewerImage.src = media.src;

            viewerImage.alt = media.title || "AWMJA Gallery";

            viewerImage.classList.add("active");

        }


        /* =================================================
           VIDEO
           ================================================= */

        else if (media.type === "video") {

            if (!viewerVideo) {
                return;
            }

            viewerVideo.src = media.src;

            viewerVideo.classList.add("active");

            viewerVideo.load();

        }


        /* =================================================
           OTHER
           ================================================= */

        else {

            console.warn(
                "Unsupported gallery media type:",
                media.type
            );

        }


        /* -----------------------------------------------
           BUTTON VISIBILITY
           ----------------------------------------------- */

        updateNavigation();

    }


    /* =====================================================
       NAVIGATION
       ===================================================== */

    function updateNavigation() {

        const multipleMedia = currentMedia.length > 1;


        if (previousButton) {

            previousButton.style.display =
                multipleMedia ? "grid" : "none";

        }


        if (nextButton) {

            nextButton.style.display =
                multipleMedia ? "grid" : "none";

        }

    }


    /* =====================================================
       NEXT MEDIA
       ===================================================== */

    function nextMedia() {

        if (!currentMedia.length) {
            return;
        }

        currentMediaIndex =
            (currentMediaIndex + 1) %
            currentMedia.length;

        updateViewer();

    }


    /* =====================================================
       PREVIOUS MEDIA
       ===================================================== */

    function previousMedia() {

        if (!currentMedia.length) {
            return;
        }

        currentMediaIndex =
            (currentMediaIndex - 1 + currentMedia.length) %
            currentMedia.length;

        updateViewer();

    }


    /* =====================================================
       ALBUM BUTTONS
       ===================================================== */

    albums.forEach((album) => {

        const openButtons =
            album.querySelectorAll(
                ".album-cover, .album-open"
            );


        openButtons.forEach((button) => {

            button.addEventListener("click", (event) => {

                event.preventDefault();

                openAlbum(album);

            });

        });

    });


    /* =====================================================
       FILTER SYSTEM
       ===================================================== */

    filters.forEach((filter) => {

        filter.addEventListener("click", () => {

            const selected =
                filter.dataset.filter || "all";


            /* ---------------------------------------------
               ACTIVE BUTTON
               --------------------------------------------- */

            filters.forEach((item) => {
                item.classList.remove("active");
            });

            filter.classList.add("active");


            /* ---------------------------------------------
               FILTER ALBUMS
               --------------------------------------------- */

            albums.forEach((album) => {

                const category =
                    album.dataset.category || "all";


                if (
                    selected === "all" ||
                    category === selected
                ) {

                    album.style.display = "";

                } else {

                    album.style.display = "none";

                }

            });

        });

    });


    /* =====================================================
       CLOSE BUTTON
       ===================================================== */

    if (closeButton) {

        closeButton.addEventListener(
            "click",
            closeAlbum
        );

    }


    /* =====================================================
       NEXT BUTTON
       ===================================================== */

    if (nextButton) {

        nextButton.addEventListener(
            "click",
            nextMedia
        );

    }


    /* =====================================================
       PREVIOUS BUTTON
       ===================================================== */

    if (previousButton) {

        previousButton.addEventListener(
            "click",
            previousMedia
        );

    }


    /* =====================================================
       CLICK OUTSIDE MEDIA
       ===================================================== */

    viewer.addEventListener("click", (event) => {

        if (event.target === viewer) {

            closeAlbum();

        }

    });


    /* =====================================================
       KEYBOARD CONTROLS
       ===================================================== */

    document.addEventListener("keydown", (event) => {

        if (!viewer.classList.contains("active")) {
            return;
        }


        /* ESC */

        if (event.key === "Escape") {

            closeAlbum();

        }


        /* RIGHT */

        if (
            event.key === "ArrowRight" ||
            event.key === "ArrowDown"
        ) {

            nextMedia();

        }


        /* LEFT */

        if (
            event.key === "ArrowLeft" ||
            event.key === "ArrowUp"
        ) {

            previousMedia();

        }

    });


    /* =====================================================
       VIDEO AUTOPAUSE
       ===================================================== */

    if (viewerVideo) {

        viewerVideo.addEventListener(
            "ended",
            () => {
                /*
                 * فعلاً بعد از پایان ویدیو
                 * کاری انجام نمی‌دهیم.
                 *
                 * در آینده می‌توانیم:
                 * - ویدیوی بعدی را اجرا کنیم
                 * - یا Replay نمایش دهیم.
                 */
            }
        );

    }


    /* =====================================================
       TOUCH / SWIPE SUPPORT
       ===================================================== */

    let touchStartX = 0;
    let touchEndX = 0;


    viewer.addEventListener(
        "touchstart",
        (event) => {

            touchStartX =
                event.changedTouches[0].screenX;

        },
        { passive: true }
    );


    viewer.addEventListener(
        "touchend",
        (event) => {

            touchEndX =
                event.changedTouches[0].screenX;

            handleSwipe();

        },
        { passive: true }
    );


    function handleSwipe() {

        const distance =
            touchEndX - touchStartX;


        /*
         * حداقل فاصله برای Swipe
         */

        if (Math.abs(distance) < 60) {
            return;
        }


        if (distance > 0) {

            previousMedia();

        } else {

            nextMedia();

        }

    }


    /* =====================================================
       DJANGO READY
       ===================================================== */

    /*
     * در مرحله Django، JavaScript نیازی به تغییر اساسی ندارد.
     *
     * Django فقط اطلاعات را داخل HTML تولید می‌کند:
     *
     * data-category
     * data-title
     * data-description
     * data-type
     * data-src
     *
     * بنابراین Backend و Frontend از هم جدا باقی می‌مانند.
     */


    console.log(
        "AWMJA Gallery initialized successfully."
    );

});