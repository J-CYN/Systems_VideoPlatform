const upBtn = document.getElementById('uploadBtn');
const upStat = document.getElementById('uploadStatus');
const grid = document.getElementById('grid');
const countEl = document.getElementById('count');
const noteEl  = document.getElementById('dashNote');

function setUploading(isUploading){ //Define IsUploading in a later send Function
    upBtn.disabled = isUploading;
    upStat.textContent = isUploading ? "Uploading! Be Patient… " : "";
    if(isUploading){
        upStat.innerHTML = '<span class="spinner" style="vertical-align:-3px"></span> Uploading…'; //Set up spinner class
    }
}

async function send(){
    const fileInput = document.getElementById('f');
    const file = fileInput.files[0];
    if(!file){ alert("Choose a file first."); return; }
    try{
        setUploading(true);
        const fd = new FormData();
        fd.append("file", file);
        const r = await fetch("/api/upload", { method: "POST", body: fd });
        const j = await r.json().catch(()=> ({}));
        if(!r.ok || !j.ok){
          throw new Error(j.error || ("Upload failed (" + r.status + ")"));
        }
        // Success: show URL and refresh the gallery without full page reload
        alert("Uploaded: " + j.url);
        fileInput.value = "";
        await loadGallery();
    }catch(err){
        console.error(err);
        alert("Upload error: " + err.message);
    }finally{
        setUploading(false);
    }
}

function renderGallery(urls){
    grid.innerHTML = "";
    if(!Array.isArray(urls) || urls.length === 0){
        countEl.textContent = "0 videos";
        noteEl.style.display = "block";
        noteEl.textContent = "No videos yet. Upload one by clicking the button on the bottom.";
        return;
    }
    noteEl.style.display = "none";
    countEl.textContent = urls.length + (urls.length === 1 ? " video" : " videos");
    for(const u of urls){
        const item = document.createElement("div");
        item.className = "item";

        const vid = document.createElement("video");
        vid.className = "thumb";
        vid.src = u;
        vid.controls = true;
        vid.muted = true;
        vid.loop = true;
        vid.autoplay = true;

        const cap = document.createElement("div");
        cap.className = "cap";
        cap.textContent = (u.split("/").pop() || u);

        item.appendChild(vid);
        item.appendChild(cap);
        grid.appendChild(item);
    }
}

async function loadGallery(){
    grid.innerHTML = '<div class="muted" style="padding:.5rem 0;"><span class="spinner"></span> Loading gallery…</div>';
    try{
        const r = await fetch("/api/catalog", { headers: { "Accept": "application/json" }});
        const j = await r.json().catch(()=> ({}));
        if(!r.ok || !j.ok){
          throw new Error(j.error || ("Failed to load gallery (" + r.status + ")"));
        }
        renderGallery(j.gallery || []);
    }catch(err){
        console.error(err);
        noteEl.style.display = "block";
        noteEl.textContent = "Could not load dashboard: " + err.message;
        grid.innerHTML = "";
        countEl.textContent = "0 videos";
    }
}

document.addEventListener("DOMContentLoaded", loadGallery);

