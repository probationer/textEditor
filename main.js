const {app, BrowserWindow, Menu, MenuItem, dialog, globalShortcut, ipcMain} = require('electron')
const path = require('path')
const url = require('url')
const fs = require('fs')
const sqlite3 = require('sqlite3').verbose();
let db = new sqlite3.Database('./database/writerBox.db', (err) => {
   if (err) {
     return console.error(err.message);
   }
   console.log('Connected to the in-memory SQlite database.');
 });

const menu = new Menu()

let win  
let root_folder = '/Users/vs/Documents/workspace@roy/text-editor/textEditor/text_files/'
      
function HomeScreen() { 
   win = new BrowserWindow({
<<<<<<< HEAD
      width: 1281, 
=======
      width: 1280, 
>>>>>>> 11fb6ffb1387eebde1a98bbc89a120eb746b83a1
      height: 800,
      icon: path.join(__dirname, 'frontend/icons/box_128x128.png')
   }) 
   win.loadURL(url.format ({ 
      pathname: path.join(__dirname, 'frontend/index.html'), 
      protocol: 'file:', 
      slashes: true
   })) 

   win.webContents.openDevTools()

   menu.append(new MenuItem({
      label: 'Print',
      accelerator: 'CommandOrControl+P',
      click: () => { console.log('time to print stuff') }
   }))
   
   //create new file
   // globalShortcut.register('CommandOrControl+N', () => {
   //    fs.writeFile('mynewfile3.txt', 'Hello content!', function (err) {
   //          if (err) throw err
   //          console.log('Saved!')
   //    })
   //    console.log('CommandOrControl+n is pressed')
   // })

   //Create new file
   ipcMain.on('item_add', (event, content) => {
      var filename;
      if (content[1] == "" ){
         filename = 'untitled'
      }else{
         filename = content[1]
      }
      //TODO : root folder must be recived here
      //check if file already exist then update that file
      filename = filename + ".txt"
      let existing_filepath =  root_folder + filename //app.getPath('/Users/vs/Documents/workspace@roy/text-editor/textEditor/text_files/')  +filename ,
      fs.access(existing_filepath, (err) => {
         if (err) {
               console.log('does not exist')
               CreateNewFIle(filename, content[0])
           } else {
               console.log('exists')
               UpdateFile(existing_filepath, content[0])
           }
       })

      if (content[0] == null){
         alert("please write something")
      }
      event.sender.send('reply', existing_filepath)
   })

}  
app.on('ready', HomeScreen)

app.on('activate', () => {
   // On macOS it's common to re-create a window in the app when the
   // dock icon is clicked and there are no other windows open.
   if (win === null) {
     createWindow()
   }
 })

app.on('will-quit', () =>{
   globalShortcut.unregisterAll();
})
 

function CreateNewFIle(filename, data, root_folder = '/Users/vs/Documents/workspace@roy/text-editor/textEditor/text_files/'){
   const option = {
      title: 'file save',
      filter: [
         {name: 'text', extensions : ['docs','txt'] }
      ],
    defaultPath: root_folder + filename //app.getPath('/Users/vs/Documents/workspace@roy/text-editor/textEditor/text_files/')  +filename ,
   }

   dialog.showSaveDialog(null ,option, (filename) =>{
      write_in_file(filename, data)
   })
}  

function UpdateFile(filename, data){
   write_in_file(filename, data)
}

function write_in_file(filename, data){
   try{
      fs.writeFile(filename, data, function (err) {
         if (err) {
            alert("error while saving file")
         }
      })
   }catch(error){
      console.log(error)
   }
}