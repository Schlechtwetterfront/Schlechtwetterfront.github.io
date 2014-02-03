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


var ID_TO_DATE = {
    'port_new': [29, 1],
    'coffs_new': [29, 1],
    'brisbane_new': [3, 2],
    'noosa_new': [3, 2],
    'hervey_new': [3, 2]
};

function checkIfNew(elementId) {
    var element = document.getElementById(elementId);
    var year = 2014;
    var month, day;
    day, month = ID_TO_DATE[elementId];
    if (element) {
        var lastVisit = getDate();
        var updated = new Date(year, month, day);
        alert(lastVisit.toGMTString());
        if (!lastVisit || (updated > lastVisit)) {
            element.className = 'hidden';
        }
    }
}


function storeDate() {
    var currentDate = new Date();
    currentDate.setTime(currentDate.getTime());
    var expiryDate = new Date();
    expiryDate.setTime(expiryDate.getTime() + (30*24*60*60*1000));
    document.cookie = 'visitDate=' + currentDate.toGMTString() + ';' + 'expire=' + expiryDate.toGMTString();
}

function storeSomeDate(day, month) {
    var year = 2014;
    var currentDate = new Date(year, month, day);
    var expiryDate = new Date();
    expiryDate.setTime(expiryDate.getTime() + (30*24*60*60*1000));
    document.cookie = 'visitDate=' + currentDate.toGMTString() + ';' + 'expire=' + expiryDate.toGMTString();
}


function getDate() {
    var cookies = document.cookie.split(';');
    var desiredKey = 'visitDate=';
    for (var i=0; i < cookies.length; i++) {
        var item = cookies[i].trim();
        if (item.indexOf(desiredKey) == 0) {
            var dateString = item.substring(desiredKey.length, item.length);
            var d = new Date(dateString);
            return d;
        }
    }
    return '';
}
