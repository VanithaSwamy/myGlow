$('.plus-cart').click(function(){
  var id=$(this).attr("sid").toString();
  var eml=this.parentNode.children[2]
  console.log("sid=",id)
  $.ajax({
    type:"GET",
    url:"/pluscart",
    data:{
      service_id:id
      //service_id:id
    },
    success:function(data){
      console.log("data =",data);
      eml.innerText=data.quantity
      document.getElementById("amount").innerText=data.amount
      document.getElementById("totalamount").innerText=data.totalamount
    }
  })
})

$('.minus-cart').click(function(){
  var id=$(this).attr("sid").toString();
  var eml=this.parentNode.children[2]
  console.log("sid=",id)
  $.ajax({
    type:"GET",
    url:"/minuscart",
    data:{
      service_id:id
    },
    success:function(data){
      console.log("data =",data);
      eml.innerText=data.quantity
      document.getElementById("amount").innerText=data.amount
      document.getElementById("totalamount").innerText=data.totalamount
    }
  })
})

$('.remove-cart').click(function(){
  var id=$(this).attr("sid").toString();
  var eml=this
  console.log("sid=",id)
  $.ajax({
    type:"GET",
    url:"/removecart",
    data:{
      service_id:id
    },
    success:function(data){
      document.getElementById("amount").innerText=data.amount
      document.getElementById("totalamount").innerText=data.totalamount
      eml.parentNode.parentNode.parentNode.parentNode.remove()
    }
  })
})