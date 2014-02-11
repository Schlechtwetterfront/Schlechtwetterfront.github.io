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


function setProjectInfo(project) {
    var header = document.getElementById('project_header');
    var body = document.getElementById('project_body');
    var project = projects[project];
    if (header) {
        header.innerHTML = project['header'];
    }
    if (body) {
        body.innerHTML = project['info'];
    }
}


function clearProjectInfo() {
    var header = document.getElementById('project_header');
    var body = document.getElementById('project_body');
    header.innerHTML = body.innerHTML = '';
}
