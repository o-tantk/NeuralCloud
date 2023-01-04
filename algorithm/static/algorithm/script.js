function setStatHidden(subClass, value) {
    var attr;
    for (var i = 0; (attr = document.getElementsByClassName("stat")[i]); ++i) {
        if (attr.classList.contains(subClass)) {
            attr.hidden = value;
        }
    }
}

function onChangeAbbr(checkbox) {
    setStatHidden("default", checkbox.checked);
    setStatHidden("abbr", !checkbox.checked);

    setCookie(checkbox.id, checkbox.checked, 30);
}

function onChangeSecondary(checkbox) {
    setStatHidden("secondary", checkbox.checked);

    setCookie(checkbox.id, checkbox.checked, 30);
}

window.onload = function (e) {
    const tokens = document.cookie.split(';');
    for (var i = 0; i < tokens.length; ++i) {
        const token = tokens[i].trim();
        const equalIndex = token.indexOf('=');
        if (equalIndex > 0) {
            const key = token.substring(0, equalIndex);
            const value = token.substring(equalIndex + 1, token.length);
            const checkbox = document.getElementById(key);
            if (checkbox) {
                checkbox.checked = value == "true";
                checkbox.onchange();
            }
        }
    }
}

//////////////////////////////////////////////
// cookie functions

function setCookie(name, value, days) {
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        var expires = "; expires=" + date.toGMTString();
    }
    else {
        expires = "";
    }

    document.cookie = name + "=" + value + expires + "; path=/";
}

/* not used
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1, c.length);
        }

        if (c.indexOf(nameEQ) == 0) {
            return c.substring(nameEQ.length, c.length);
        }
    }

    return null;
}
*/
