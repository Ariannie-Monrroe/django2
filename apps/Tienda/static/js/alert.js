// $(document).ready(function(){
//     $("#alertSI").hide();
//     $("#alertNO").hide();
//     $("#form1").submit(function(e){
//         e.preventDefault();
//         txtSku= $.trim($("#txtSku").val());
//         txtnombre= $.trim($("#txtnombre").val());
//         txtprecio= $.trim($("#txtprecio").val());
//         txtStock= $.trim($("#txtStock").val());
//         txtDescripcion= $.trim($("#txtDescripcion").val());
//         if (txtSku.length>0 &&  txtnombre.length>0 && txtprecio.length>0 && txtStock.length>0 && txtDescripcion.length>0) {
//             $("#alertSI").fadeTo(2000, 500).slideUp(500, function() {
//                 $("#alertSI").slideUp(500);
//             });
//         } else{
//             $("#alertNO").fadeTo(2000, 500).slideUp(500, function() {
//                 $("#alertNO").slideUp(500);
//             });
//         }
//     });
// });