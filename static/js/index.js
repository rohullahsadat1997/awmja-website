/* =========================================
   AWMJA — INDEX JAVASCRIPT
   ========================================= */

document.addEventListener("DOMContentLoaded", () => {

    console.log("AWMJA JS LOADED");


    /* =====================================
       MOBILE MENU
       ===================================== */

    const menuToggle =
        document.querySelector(".menu-toggle");

    const mobileMenu =
        document.querySelector(".mobile-menu");

    const body =
        document.body;


    if (menuToggle && mobileMenu) {

        menuToggle.addEventListener("click", () => {

            const isOpen =
                mobileMenu.classList.toggle("open");

            menuToggle.classList.toggle(
                "active",
                isOpen
            );

            body.classList.toggle(
                "menu-open",
                isOpen
            );

            menuToggle.setAttribute(
                "aria-expanded",
                isOpen
            );

        });


        /* Close mobile menu */

        const mobileLinks =
            mobileMenu.querySelectorAll("a");


        mobileLinks.forEach(link => {

            link.addEventListener("click", () => {

                mobileMenu.classList.remove("open");

                menuToggle.classList.remove("active");

                body.classList.remove("menu-open");

                menuToggle.setAttribute(
                    "aria-expanded",
                    "false"
                );

            });

        });

    }


    /* =====================================
       MOBILE LANGUAGE
       ===================================== */

    const mobileLanguages =
        document.querySelectorAll(
            ".mobile-language .language-btn"
        );


    mobileLanguages.forEach(button => {

        button.addEventListener("click", () => {

            mobileLanguages.forEach(btn => {

                btn.classList.remove(
                    "active-lang"
                );

            });

            button.classList.add(
                "active-lang"
            );

        });

    });


    /* =====================================
       DESKTOP LANGUAGE
       ===================================== */

    const desktopLanguages =
        document.querySelectorAll(
            ".nav-actions .language-btn"
        );


    desktopLanguages.forEach(button => {

        button.addEventListener("click", () => {

            desktopLanguages.forEach(btn => {

                btn.classList.remove(
                    "active-lang"
                );

            });

            button.classList.add(
                "active-lang"
            );

        });

    });


    /* =====================================
       HEADER SCROLL EFFECT
       ===================================== */

    const header =
        document.querySelector(".site-header");


    if (header) {

        const updateHeader = () => {

            if (window.scrollY > 40) {

                header.classList.add(
                    "scrolled"
                );

            } else {

                header.classList.remove(
                    "scrolled"
                );

            }

        };


        window.addEventListener(
            "scroll",
            updateHeader,
            {
                passive: true
            }
        );


        updateHeader();

    }


    /* =====================================
       SCROLL REVEAL
       ===================================== */

    const revealElements =
        document.querySelectorAll(
            ".section, .work-card, .news-card, .event-item, .gallery-item"
        );


    if (
        revealElements.length &&
        "IntersectionObserver" in window
    ) {

        const revealObserver =
            new IntersectionObserver(
                (entries, observer) => {

                    entries.forEach(entry => {

                        if (
                            entry.isIntersecting
                        ) {

                            entry.target.classList.add(
                                "reveal-visible"
                            );

                            observer.unobserve(
                                entry.target
                            );

                        }

                    });

                },
                {
                    threshold: 0.12
                }
            );


        revealElements.forEach(element => {

            element.classList.add(
                "reveal-hidden"
            );

            revealObserver.observe(
                element
            );

        });

    }


    /* =====================================
       HERO PARALLAX
       ===================================== */

    const heroVisual =
        document.querySelector(
            ".hero-visual"
        );


    if (heroVisual) {

        window.addEventListener(
            "scroll",
            () => {

                const scroll =
                    window.scrollY;


                if (scroll < 700) {

                    heroVisual.style.transform =
                        `translateY(${scroll * 0.08}px)`;

                }

            },
            {
                passive: true
            }
        );

    }


    /* =====================================
       CURRENT YEAR
       ===================================== */

    const yearElements =
        document.querySelectorAll(
            ".current-year"
        );


    yearElements.forEach(element => {

        element.textContent =
            new Date().getFullYear();

    });


    /* =====================================
       IMPACT COUNTERS
       ===================================== */

    const counters =
        document.querySelectorAll(
            ".counter"
        );


    if (
        counters.length &&
        "IntersectionObserver" in window
    ) {

        const counterObserver =
            new IntersectionObserver(
                (entries, observer) => {

                    entries.forEach(entry => {

                        if (
                            !entry.isIntersecting
                        ) {
                            return;
                        }


                        const counter =
                            entry.target;


                        const target =
                            Number(
                                counter.dataset.target
                            );


                        if (
                            Number.isNaN(target)
                        ) {
                            return;
                        }


                        const duration =
                            1800;


                        const startTime =
                            performance.now();


                        function animate(
                            currentTime
                        ) {

                            const progress =
                                Math.min(
                                    (
                                        currentTime -
                                        startTime
                                    ) / duration,
                                    1
                                );


                            const eased =
                                1 -
                                Math.pow(
                                    1 - progress,
                                    3
                                );


                            const value =
                                Math.floor(
                                    eased * target
                                );


                            counter.textContent =
                                value.toLocaleString();


                            if (
                                progress < 1
                            ) {

                                requestAnimationFrame(
                                    animate
                                );

                            } else {

                                counter.textContent =
                                    target.toLocaleString();

                            }

                        }


                        requestAnimationFrame(
                            animate
                        );


                        observer.unobserve(
                            counter
                        );

                    });

                },
                {
                    threshold: 0.2
                }
            );


        counters.forEach(counter => {

            counterObserver.observe(
                counter
            );

        });

    }

});