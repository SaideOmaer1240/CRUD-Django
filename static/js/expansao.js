/* Adicionar cor no menu selecionado */
var menuItem = document.querySelectorAll('.item-menu')
function selectLink(){
    menuItem.forEach((item)=>
    item.classList.remove('ativo')
    )
    this.classList.add('ativo')
}

menuItem.forEach((item)=>
    item.addEventListener('click', selectLink)
)

/* Expadir ou diminuir sidebar */
document.getElementById('btn-exp').addEventListener('click', function() {
  document.querySelector('.container_partial').classList.toggle('expandir');
  if (document.querySelector('.container_partial').classList.contains('expandir')) {
    document.querySelectorAll('.txt-link').forEach(function(link) {
      link.style.opacity = '1';
    
    });
  } else {
    document.querySelectorAll('.txt-link').forEach(function(link) {
      link.style.opacity = '0';
    });
     
  }
});
