
/*
	* Page functionality.
	*
*/


function pad(pad, str, padLeft) {
  if (typeof str === 'undefined') 
    return pad;
  if (padLeft) {
    return (pad + str).slice(-pad.length);
  } else {
    return (str + pad).substring(0, pad.length);
  }
}


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


function calculateSidebarListHeight() {
	var total_height_children = 0;
	var total_height_sidebar = $(".sidebar").height();
	var sidebar_padding_bottom = parseInt($(".sidebar").css("padding-bottom"));
	var scrollable = null;
	var scrollable_min_height = 100; // Min height for any scrollable list inside the sidebar.


	$(".sidebar").children().each(function() {
		if ($(this).attr("id") != "sidebar-content") {
			total_height_children += $(this).outerHeight(true);
		}
	});

	$("#sidebar-content").css("height", total_height_sidebar - total_height_children - sidebar_padding_bottom + "px");

	$("#sidebar-content").children().each(function() {
		if ($(this).attr("class") == "sidebar-content-scrollable") {
			$(this).css("height", total_height_sidebar - total_height_children - sidebar_padding_bottom + "px");
			scrollable = $(this);
		} else {
			total_height_children += $(this).outerHeight(true);
		}
	});

	if (total_height_children + scrollable_min_height > total_height_sidebar) {
		$("#sidebar-content").addClass("sidebar-content-scrollable");
		if (scrollable != null) {
			scrollable.css("height", "auto");
		}
	} else {
		$("#sidebar-content").removeClass("sidebar-content-scrollable");
	}
}


window.addEventListener("load", function() {

	calculateSidebarListHeight();

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


    $("a.rectangle-button").click(function() {
        var id = $(this).attr("href");
        showContent(id);
    });


    var indent_width = "2px";
    indent_width = $("indent-child").css("width");

    $("a.rectangle-button").hover(
        function() {
            $(this).children("indent-child").css({"visibility": "hidden"});
            // $(this).children("indent-child").stop().animate({"width": 0}, {
            //     duration: 300,
            //     fail: function() { $(this).css("visibility", "visible"); }
            // });
        },
        function() {
            $(this).children("indent-child").css({"visibility": "visible", "width": indent_width});
            // $(this).children("indent-child").stop().animate({"width": indent_width}, {
            //     duration: 300,
            //     always: function() { $(this).css("visibility", "visible"); }
            // });
        }
    );


    // flag calc
    function setHex(hex) {
    	if (hex.length < 2) {
    		hex = pad("00", hex, true);
    	}
    	$("#flag-hex-value").prop("value", hex);
    }


    function setInt(value) {
    	$("#flag-int-value").prop("value", value);
    }

    function setFlags(value) {
    	$("togglebox").each(function() {
			var box_value = parseInt($(this).attr("value"));
			$(this).attr("toggled", (value & box_value) ? "true" : "false");
			$(this).trigger("toggle-state-changed");
		});
    }

	$("#convert-from-value").click(function() {
		var value = parseInt($("#flag-int-value").prop("value"));
		if (!isNaN(value)) {
			setHex(value.toString(16));
			setFlags(value);
		}
	});


	$("#convert-from-hex").click(function() {
		var value = parseInt($("#flag-hex-value").prop("value"), 16);
		if (!isNaN(value)) {
			setInt(value);
			setFlags(value);
		}
	});


	$("#convert-from-flags").click(function() {
		var value = 0;
		$("togglebox").each(function() {
			var box_value = parseInt($(this).attr("value"));
			if ($(this).attr("toggled") == "true") {
				value += box_value;
			}
		});
		setHex(value.toString(16));
		setInt(value);
	});
});


$(window).resize(function () {
	calculateSidebarListHeight();
});


$(document).ready(function () {
    var parts = window.location.href.split("#");
    if(parts.length > 1) {
       var id = parts[ parts.length-1 ];
       showContent(id);
    }
});
