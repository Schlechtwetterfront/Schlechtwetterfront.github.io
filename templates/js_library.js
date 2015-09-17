function slideToggleContent(id) {
    if (id.substr(0, 1) != "#") {
        id = "#" + id;
    }
    var content = id + "_content";

    $(content).slideToggle(250, function () {
        $(content + "_start").text(function () {
            return $(content).is(":visible") ? "Collapse" : "Expand";
        })
    });
}

function showContent(id) {
    if (id.substr(0, 1) != "#") {
        id = "#" + id;
    }
    var content = id + "_content";
    if ($(content).is(":visible")) {
        return;
    }
    $(content).slideToggle(250, function () {
        $(content + "_start").text(function () {
            return $(content).is(":visible") ? "Collapse" : "Expand";
        })
    });
}

$("a.toggle_collapse").click(function () {
    var header = $(this);
    var content = $("#" + $(this).attr("content-id"));

    $(content).slideToggle(250, function () {

        header.text(function () {

            return $(content).is(":visible") ? "Collapse" : "Expand";
        });
    });

});

$("a.toggle_collapse_end").click(function () {
    var header = $(this);
    var content_text = "#" + $(this).attr("content-id");
    var content = $("#" + $(this).attr("content-id"));

    $(content).slideToggle(250, function () {
        $(content_text + "_start").text(function () {
            return $(content).is(":visible") ? "Collapse" : "Expand";
        })
    });

});

$("a.toggle_collapse").each(function () {
    var header = $(this);
    var content = $("#" + $(this).attr("content-id"));

    if ($(this).attr("starts-collapsed") == "True") {
        $(content).slideToggle(0, function () {

            header.text(function () {

                return $(content).is(":visible") ? "Collapse" : "Expand";
            });
        });
    }
});


$("a.rectangle_button").click(function() {
    var id = $(this).attr("href");
    showContent(id);
});


$(document).ready(function () {
    var parts = window.location.href.split("#");
    if(parts.length > 1) {
       var id = parts[ parts.length-1 ];
       showContent(id);
    }
});
