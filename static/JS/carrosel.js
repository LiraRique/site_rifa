var timer;

$(function(){
    $('.slide img:eq(0)').addClass("ativo").show();
    var texto= $(".ativo").attr("alt");
    $('.slide').prepend("");


slide();

function slide(){
    var $NEXT= $();
    var $ATUAL= $('.ativo');
    if($('.ativo').next().length){
        $NEXT =$('.ativo').next();
    }
     else{
         $NEXT =$('.slide img:eq(0)');
         }
    timer =$ATUAL.data('timer')


setTimeout(function() {

$ATUAL.fadeOut().removeClass("ativo");

$NEXT.fadeIn().addClass("ativo");


var texto
= $NEXT.attr('alt');

$('.slide p').hide().html(texto).delay(0.5).fadeIn();


slide();

}, timer);

}

});


function alerta_compra()
{
    var x;
    var r=confirm("Confirmar os numeros selecionados ! se estiver corretos clique em ok ");
    if (r==true)
      {
      x="você pressionou OK!";
      window.location="http://www.devmedia.com.br/";
      }
    else
      {
      x="Você pressionou Cancelar!";
      }
    document.getElementById("demo").innerHTML=x;
}
