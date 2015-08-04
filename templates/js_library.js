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
