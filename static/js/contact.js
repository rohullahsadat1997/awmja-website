
/* =========================================================
   AWMJA — CONTACT PAGE JAVASCRIPT
   Frontend Form Validation
   Django Ready
   ========================================================= */

document.addEventListener("DOMContentLoaded", function () {

    /* =====================================================
       CONTACT FORM
       ===================================================== */

    const contactForm = document.querySelector("#contactForm");

    if (!contactForm) {
        return;
    }


    /* =====================================================
       FORM ELEMENTS
       ===================================================== */

    const nameInput = contactForm.querySelector("#name");
    const emailInput = contactForm.querySelector("#email");
    const subjectInput = contactForm.querySelector("#subject");
    const messageInput = contactForm.querySelector("#message");

    const submitButton = contactForm.querySelector(
        ".contact-submit"
    );

    const statusMessage = contactForm.querySelector(
        ".form-status"
    );


    /* =====================================================
       EMAIL VALIDATION
       ===================================================== */

    function isValidEmail(email) {

        const emailPattern =
            /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        return emailPattern.test(email);
    }


    /* =====================================================
       SHOW STATUS
       ===================================================== */

    function showStatus(message, type) {

        if (!statusMessage) {
            return;
        }

        statusMessage.textContent = message;

        statusMessage.classList.remove(
            "success",
            "error"
        );

        statusMessage.classList.add(type);

        statusMessage.scrollIntoView({
            behavior: "smooth",
            block: "center"
        });
    }


    /* =====================================================
       CLEAR STATUS
       ===================================================== */

    function clearStatus() {

        if (!statusMessage) {
            return;
        }

        statusMessage.textContent = "";

        statusMessage.classList.remove(
            "success",
            "error"
        );
    }


    /* =====================================================
       REMOVE INPUT ERROR
       ===================================================== */

    function clearInputError(input) {

        if (!input) {
            return;
        }

        input.classList.remove("input-error");
    }


    /* =====================================================
       SHOW INPUT ERROR
       ===================================================== */

    function showInputError(input) {

        if (!input) {
            return false;
        }

        input.classList.add("input-error");

        input.focus();

        return false;
    }


    /* =====================================================
       CLEAR ERROR WHILE USER TYPES
       ===================================================== */

    [
        nameInput,
        emailInput,
        subjectInput,
        messageInput
    ].forEach(function (input) {

        if (!input) {
            return;
        }

        input.addEventListener("input", function () {

            clearInputError(input);

            clearStatus();

        });

    });


    /* =====================================================
       FORM SUBMIT
       ===================================================== */

    contactForm.addEventListener(
        "submit",
        function (event) {

            /*
             * Prevent normal browser submission.
             *
             * Later, when Django is connected,
             * this section can be replaced with
             * fetch() / API submission.
             */

            event.preventDefault();


            /* ---------------------------------------------
               CLEAR PREVIOUS STATUS
               --------------------------------------------- */

            clearStatus();


            /* ---------------------------------------------
               GET VALUES
               --------------------------------------------- */

            const name =
                nameInput
                    ? nameInput.value.trim()
                    : "";

            const email =
                emailInput
                    ? emailInput.value.trim()
                    : "";

            const subject =
                subjectInput
                    ? subjectInput.value.trim()
                    : "";

            const message =
                messageInput
                    ? messageInput.value.trim()
                    : "";


            /* ---------------------------------------------
               VALIDATE NAME
               --------------------------------------------- */

            if (name.length < 2) {

                showInputError(nameInput);

                showStatus(
                    "لطفاً نام خود را به‌درستی وارد کنید.",
                    "error"
                );

                return;
            }


            /* ---------------------------------------------
               VALIDATE EMAIL
               --------------------------------------------- */

            if (!isValidEmail(email)) {

                showInputError(emailInput);

                showStatus(
                    "لطفاً یک آدرس ایمیل معتبر وارد کنید.",
                    "error"
                );

                return;
            }


            /* ---------------------------------------------
               VALIDATE SUBJECT
               --------------------------------------------- */

            if (subject.length < 3) {

                showInputError(subjectInput);

                showStatus(
                    "لطفاً موضوع پیام را وارد کنید.",
                    "error"
                );

                return;
            }


            /* ---------------------------------------------
               VALIDATE MESSAGE
               --------------------------------------------- */

            if (message.length < 10) {

                showInputError(messageInput);

                showStatus(
                    "لطفاً پیام خود را کامل‌تر بنویسید.",
                    "error"
                );

                return;
            }


            /* ---------------------------------------------
               DISABLE SUBMIT BUTTON
               --------------------------------------------- */

            if (submitButton) {

                submitButton.disabled = true;

                submitButton.dataset.originalText =
                    submitButton.innerHTML;

                submitButton.innerHTML = `
                    <span>در حال بررسی...</span>
                    <i class="fa fa-spinner fa-spin"></i>
                `;

            }


            /* =================================================
               TEMPORARY FRONTEND SUCCESS
               =================================================

               IMPORTANT:

               This DOES NOT send the message to the server.

               It is only for testing the frontend.

               Later Django will replace this section.
               ================================================= */

            setTimeout(function () {

                showStatus(
                    "پیام شما با موفقیت ثبت شد. از تماس شما سپاسگزاریم.",
                    "success"
                );


                /* ---------------------------------------------
                   RESET FORM
                   --------------------------------------------- */

                contactForm.reset();


                /* ---------------------------------------------
                   RESTORE BUTTON
                   --------------------------------------------- */

                if (submitButton) {

                    submitButton.disabled = false;

                    submitButton.innerHTML =
                        submitButton.dataset.originalText;

                }

            }, 900);

        }
    );


    /* =====================================================
       PREVENT DOUBLE SUBMISSION
       ===================================================== */

    if (submitButton) {

        submitButton.addEventListener(
            "click",
            function () {

                if (submitButton.disabled) {

                    return;

                }

            }
        );

    }

});

