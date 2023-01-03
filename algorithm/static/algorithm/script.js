function applyHidden(statStyle) {
    var attr;
    for (var i = 0; (attr = document.getElementsByClassName("stat")[i]); ++i) {
        attr.hidden = !attr.classList.contains(statStyle);
    }
}

// TODO: vary for secondary stat
function onChangeCheckbox(checkbox) {
    if (checkbox.checked) {
        applyHidden("abbr");
    }
    else {
        applyHidden("default");
    }

    setCookie("stat_style", checkbox.checked, 30)
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
    const statStyle = getCookie("stat_style");
    if (statStyle) {
        const checkbox = document.getElementById("stat_style");
        checkbox.checked = statStyle == "true";
        checkbox.onchange();
    }
}