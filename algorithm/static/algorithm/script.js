function changeStyleSheet(name) {
    var attr;
    
    /*
    for (var i = 0; (attr = document.getElementsByTagName("link")[i]); ++i) {
        if (attr.getAttribute("rel") == "stylesheet") {
            const href = attr.getAttribute("href").replace(/(?!.*\/).*(?=\.css)/, name);
            attr.setAttribute("href", href);
        }
    }
    */

    for (var i = 0; (attr = document.getElementsByClassName("stat")[i]); ++i) {
        const show = attr.classList.contains(name);
        attr.hidden = !show;
    }

    setCookie("style", name, 30)
}

function onChangeCheckbox(checkbox) {
    if (checkbox.checked) {
        changeStyleSheet("style_abbr");
    }
    else {
        changeStyleSheet("style");
    }
}

function setCookie(name, value, days) {
    if (days) {
      var date = new Date();
      date.setTime(date.getTime()+(days*24*60*60*1000));
      var expires = "; expires="+date.toGMTString();
    }
    else {
        expires = "";
    }

    document.cookie = name + "=" + value + expires + "; path=/";
}
  
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') {
            c = c.substring(1,c.length);
        }

        if (c.indexOf(nameEQ) == 0) {
            return c.substring(nameEQ.length,c.length);
        } 
    }

    return null;
}

window.onload = function(e) {
    const styleName = getCookie("style");
    if (styleName) {
        const checkbox = document.getElementById(styleName);
        if (checkbox) {
            checkbox.checked = true;
            checkbox.onchange();
        }
    }
}