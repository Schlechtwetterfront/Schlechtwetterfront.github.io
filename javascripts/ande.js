function toggleHide(divID) {
    var item = document.getElementById(divID);
    if (item) {
        item.className = (item.className == 'hidden') ? 'unhidden' : 'hidden';
    }
}


var projects = {
    'zet': {'header': 'XSIZETools', 'info': 'ZeroEngine .msh exporter and importer for Softimage'},
    'softcry': {'header': 'SoftCry', 'info': 'CRYENGINE exporter for Softimage'},
    'modosrcr': {'header': 'modosourcerer', 'info': 'Source Engine exporter for modo'},
    'zefrmt': {'header': 'ZeroEngine Docs', 'info': 'Information about ZeroEngine file formats'}
};


var platforms = {
    'github': {'header': 'GitHub', 'info': 'Look my code'},
    'twitter': {'header': 'Twitter', 'info': 'Follow me on Twitter'},
    'steam': {'header': 'Steam', 'info': 'Go and increase my self-esteam!'},
    //'zefrmt': {'header': 'ZeroEngine Docs', 'info': 'Information about ZeroEngine file formats'}
};


function setProjectInfo(project) {
    var header = document.getElementById('project_header');
    var body = document.getElementById('project_body');
    var project = projects[project];
    if (header) {
        header.innerHTML = project['header'];
        header.style.opacity = 1;
    }
    if (body) {
        body.innerHTML = project['info'];
        body.style.opacity = 1;
    }
}


function setSocialInfo(platform) {
    var header = document.getElementById('social_header');
    var body = document.getElementById('social_body');
    var social = platforms[platform];
    if (header) {
        header.innerHTML = social['header'];
        header.style.opacity = 1;
    }
    if (body) {
        body.innerHTML = social['info'];
        body.style.opacity = 1;
    }
}


function clearProjectInfo() {
    var header = document.getElementById('project_header');
    var body = document.getElementById('project_body');
    header.style.opacity = body.style.opacity = 0;
}


function clearSocialInfo() {
    var header = document.getElementById('social_header');
    var body = document.getElementById('social_body');
    header.style.opacity = body.style.opacity = 0;
}
