/**
 * We'll load the axios HTTP library which allows us to easily issue requests
 * to our back-end. This library automatically handles sending the
 * CSRF token as a header based on the value of the "XSRF" token cookie.
 */

window.axios = require("axios");

let token = document.querySelector('[name=csrfmiddlewaretoken]').value;
if (token) {
    window.axios.defaults.headers.common["X-CSRFToken"] = token;
} else {
    console.error("CSRF token not found");
}