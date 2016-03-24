
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
    function setHex(hex, group) {
    	if (hex.length < 2) {
    		hex = pad("00", hex, true);
    	}
        if (group == "flag") {
    	   $("#flag-hex-value").prop("value", hex);
        } else if (group == "rendertype") {
            $("#render-type-hex-value").prop("value", hex);
        } else if (group == "data0") {
            $("#data0-hex-value").prop("value", hex);
        } else if (group == "data1") {
            $("#data1-hex-value").prop("value", hex);
        }
    }


    function setInt(value, group) {
        if (group == "flag") {
           $("#flag-int-value").prop("value", value);
        } else if (group == "rendertype") {
            $("#render-type-int-value").prop("value", value);
        } else if (group == "data0") {
            $("#data0-int-value").prop("value", value);
        } else if (group == "data1") {
            $("#data1-int-value").prop("value", value);
        }
    }

    function setFlags(value) {
    	$(".togglebox-flags").each(function() {
			var box_value = parseInt($(this).attr("value"));
			$(this).attr("toggled", (value & box_value) ? "true" : "false");
			$(this).trigger("toggle-state-changed");
		});
    }

	$("#convert-from-value").click(function() {
		var value = parseInt($("#flag-int-value").prop("value"));
		if (!isNaN(value)) {
			setHex(value.toString(16), "flag");
			setFlags(value);
		}
	});


	$("#convert-from-hex").click(function() {
		var value = parseInt($("#flag-hex-value").prop("value"), 16);
		if (!isNaN(value)) {
			setInt(value, "flag");
			setFlags(value);
		}
	});


	$("#convert-from-flags").click(function() {
		var value = 0;
		$(".togglebox-flags").each(function() {
			var box_value = parseInt($(this).attr("value"));
			if ($(this).attr("toggled") == "true") {
				value += box_value;
			}
		});
		setHex(value.toString(16), "flag");
		setInt(value, "flag");
	});


    $("#render-type-select").change(function() {
        var val = parseInt($("#render-type-select").prop("value"), 10).toString(16);
        setHex(val, "rendertype");
    });


    $("#render-type-hex-value").change(function() {
        var val = $("#render-type-hex-value").prop("value");
        $("#render-type-select").prop("value", parseInt(val, 16));
    });


    $("#data0-int-value").change(function() {
        var value = parseInt($("#data0-int-value").prop("value"), 10);
        setHex(value.toString(16), "data0");
    });


    $("#data0-hex-value").change(function() {
        var value = parseInt($("#data0-hex-value").prop("value"), 16);
        setInt(value.toString(), "data0");
    });


    $("#data1-int-value").change(function() {
        var value = parseInt($("#data1-int-value").prop("value"), 10);
        setHex(value.toString(16), "data1");
    });


    $("#data1-hex-value").change(function() {
        var value = parseInt($("#data1-hex-value").prop("value"), 16);
        setInt(value.toString(), "data1");
    });


    $("#gather-all").click(function() {
        var chunk = "41 54 52 42 04 00 00 00 ";
        chunk += $("#flag-hex-value").prop("value") + " ";
        chunk += $("#render-type-hex-value").prop("value") + " ";
        chunk += $("#data0-hex-value").prop("value") + " ";
        chunk += $("#data1-hex-value").prop("value");
        if ($("#buildWithSpaces").attr("toggled") != "true") {
            chunk = chunk.replace(/ /g, "");
        }
        $("#result").prop("value", chunk);
    });


    $("#from-all").click(function() {
        var chunk = $("#result").prop("value");
        if (chunk.length > 24) {
            chunk = chunk.replace(/ /g, "");
        }
        var flag = chunk.substring(16, 18);
        var renderType = chunk.substring(18, 20);
        var data0 = chunk.substring(20, 22);
        var data1 = chunk.substring(22, 24);

        setHex(flag, "flag");
        setHex(renderType, "rendertype");
        setHex(data0, "data0");
        setHex(data1, "data1");

        $("#render-type-hex-value, #data0-hex-value, #data1-hex-value").change();
        $("#convert-from-hex").click();
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
