const {app, BrowserWindow, Menu, MenuItem, dialog} = require('electron')
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
      accelerator: 'CmdOrCtrl+P',
      click: () => { console.log('time to print stuff') }
   }))

   //open file
   globalShortcut.register('CommandOrControl+o', () => {
      dialog.showOpenDialog({ properties: ['openFile'] })
      console.log('CommandOrControl+o is pressed')
   })
   
   //create new file
   globalShortcut.register('CommandOrControl+N', () => {
      fs.writeFile('mynewfile3.txt', 'Hello content!', function (err) {
            if (err) throw err
            console.log('Saved!')
      })
      console.log('CommandOrControl+n is pressed')
   })


   const options_to_save_file = {
      defaultPath: app.getPath('documents') + '/file.pdf',
   }


   globalShortcut.register('CommandOrControl+S', () => {
      dialog.showSaveDialog(null, options_to_save_file, (path) => {
         console.log(path);
         console.log(options_to_save_file);
      });
      console.log('CommandOrControl+S is pressed')
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
 