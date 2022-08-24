const pianokeys = document.querySelectorAll('.key')
function sound(link){
new Audio(link).play()
console.log(link)
}
pianokeys.forEach((key,i)=>{
    const number = i<9?'0'+(i+1):(i+1)
    const link = 'keys/key'+number+'.mp3'
    key.addEventListener('click',()=>sound(link))
})