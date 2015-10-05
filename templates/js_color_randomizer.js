function shadeBlend(p,c0,c1) {
    var n=p<0?p*-1:p,u=Math.round,w=parseInt;
    if(c0.length>7){
        var f=c0.split(","),t=(c1?c1:p<0?"rgb(0,0,0)":"rgb(255,255,255)").split(","),R=w(f[0].slice(4)),G=w(f[1]),B=w(f[2]);
        return "rgb("+(u((w(t[0].slice(4))-R)*n)+R)+","+(u((w(t[1])-G)*n)+G)+","+(u((w(t[2])-B)*n)+B)+")"
    }else{
        var f=w(c0.slice(1),16),t=w((c1?c1:p<0?"#000000":"#FFFFFF").slice(1),16),R1=f>>16,G1=f>>8&0x00FF,B1=f&0x0000FF;
        return "#"+(0x1000000+(u(((t>>16)-R1)*n)+R1)*0x10000+(u(((t>>8&0x00FF)-G1)*n)+G1)*0x100+(u(((t&0x0000FF)-B1)*n)+B1)).toString(16).slice(1)
    }
}

var colors = [
    "#ff7676", // reddish
    // "#8d76ff", // darker violet
    // "#d77f64", // orange
    "#919ddb", // brighter blue
    "#6AAF6A", // green
];


window.addEventListener("load", function() {

    // Choose random hover color for all elments.
    var box_hover_color = colors[Math.floor(Math.random() * colors.length)];

    var box_darkened_color = shadeBlend(-0.3, box_hover_color);

    var box_brightened_color = shadeBlend(0.5, box_hover_color);

    var box_normal_color = "#252525";

    // I LOVE HACKS FeelsGoodMan
    var theme_map = {
        "rgb(255, 255, 255)": "bright",
        "rgb(0, 0, 0)": "dark",
    };

    var bg_color = $("head").css("background-color");
    var theme = theme_map[bg_color];

    var link_color_map_hover = {
        "bright": box_darkened_color,
        "dark": box_brightened_color,
    };

    $("div.content a").css({"color": box_hover_color, "border-bottom": "1px dotted " + box_hover_color});
    $("div.content a").hover(
    	function() {
    		$(this).css({"color": link_color_map_hover[theme],
    					"border-bottom": "1px solid " + link_color_map_hover[theme]});
    	},
    	function() {
    		$(this).css({"color": box_hover_color,
    					"border-bottom": "1px dotted " + box_hover_color,
    					"text-decoration": "none"});
    	}
    );
});

