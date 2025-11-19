const upBtn = document.getElementById('uploadBtn');
const upStat = document.getElementById('uploadStatus');

function setUploading(isUploading){ //Define IsUploading in a later send Function
    upBtn.disabled = isUploading;
    upStat.textContent = isUploading ? "Uploading! Be Patient… " : "";
    if(isUploading){
        upStat.innerHTML = '<span class="spinner" style="vertical-align:-3px"></span> Uploading…'; //Set up spinner class
    }
    }

//Continue Javascript Code