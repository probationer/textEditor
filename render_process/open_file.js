const {globalShortcut,app,dialog} = require('electron').remote;
const fs = require("fs")


//read file from system
globalShortcut.register('CommandOrControl+O', (event) =>{
    dialog.showOpenDialog((filename) => {
        // fileNames is an array that contains all the selected
        if(filename === undefined){
            console.log("No file selected")
        }
        filepath = filename[0]
        var filedata
        fs.readFile(filepath, 'utf-8', (err, data) => {
            if(err){
                console.log("An error ocurred reading the file : " + err.message)
            }
            console.log(data+":\n" +filepath.split('/').pop())
            document.getElementById('file_name').value = filepath.split('/').pop()
            tinymce.activeEditor.setContent(data);
        })
    })
})