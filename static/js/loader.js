/* =========================================
   AWMJA — PAGE LOADER
   ========================================= */

(function () {

    const loader = document.getElementById("page-loader");

    if (!loader) {
        return;
    }


    /* =========================================
       PAGE LOADED
       ========================================= */

    window.addEventListener("load", function () {

        // یک مکث کوتاه برای نمایش زیبای Loader
        setTimeout(function () {

            loader.style.opacity = "0";
            loader.style.visibility = "hidden";
            loader.style.pointerEvents = "none";

        }, 2500);

    });


    /* =========================================
       SAFETY FALLBACK
       جلوگیری از گیر کردن Loader
       ========================================= */

    setTimeout(function () {

        loader.style.opacity = "0";
        loader.style.visibility = "hidden";
        loader.style.pointerEvents = "none";

    }, 5000);


})();


