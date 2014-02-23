function toggle(prefix) {
    var content_item = document.getElementById(prefix + '_content');
    var toggler_item = document.getElementById(prefix + '_toggler')
    if (content_item) {
        content_item.className = (content_item.className == 'hidden') ? 'unhidden' : 'hidden';
    }
    if (toggler_item) {
        toggler_item.innerHTML = (toggler_item.innerHTML == 'Anzeigen') ? 'Verbergen' : 'Anzeigen';
    }
}
