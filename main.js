const {app, BrowserWindow, Menu, MenuItem, dialog, globalShortcut, ipcMain} = require('electron')
const path = require('path')
const url = require('url')
const fs = require('fs')
const menu = new Menu()

let win  

function HomeScreen() { 
   win = new BrowserWindow({width: 800, height: 600}) 
   win.loadURL(url.format ({ 
      pathname: path.join(__dirname, 'frontend/index.html'), 
      protocol: 'file:', 
      slashes: true
   })) 

   // win.webContents.openDevTools()

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
      
      //check if file already exist then update that file
      filename = filename + ".txt"
      let existing_filepath = app.getPath('documents') +'/' +filename
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
         alert("please writesomething")
      }
      event.sender.send('reply', filename)
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
 

function CreateNewFIle(filename, data){
   const option = {
      title: 'file save',
      filter: [
         {name: 'text', extensions : ['docs','txt'] }
      ],
    defaultPath: app.getPath('documents') +'/' +filename ,
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