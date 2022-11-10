
<template>
  <div id="app" style="height:auto;" class="row">
      <div class='box col-3 m-2 p-2'><SideBar/></div>
      <div class="box-in col-8 m-2 p-2"><router-view /></div>
    </div>
</template>
<script>
import SideBar from '@/components/SideBar'
export default  {
  components : {
    SideBar,
  }
}

</script>

<!-- <script language="JavaScript" type="text/javascript">
$(document).ready(function(){ 
    $('selector').css('width', $(window).width()); 
    $('selector').css('height', $(window).height()); 
    $(window).resize(function() { 
        $('selector').css('width', $(window).width()); 
        $('selector').css('height', $(window).height()); 
    }); 
});
</script> -->
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.box {
  border : 1px solid black;
  /* overflow: auto; */
  width:30%;
  float:left;
  /* margin:0 auto; */
  /* height:100%; */
  /* align-items: center;
  display: flex;
  justify-content: center; */
  border-radius: 15px 15px 15px 15px;
  margin-bottom: 400px;

}
.box-in {
  border : 1px solid;
  /* overflow: auto; */
  width:60%;
  float:right;
  /* margin:0 auto; */
  /* height: 100%; */
  /* align-items: center;
  display: flex;
  justify-content: center; */
  border-radius: 15px 15px 15px 15px;
  padding: 10px;
}
.important {
  margin: 15px 0px 5px 0px;
  padding: 30px;
  border:1px solid;
  border-radius: 15px 15px 15px 15px;
  width : 100%;
}

.sidebarBox {
	margin-top: -9999px;
	margin-bottom: -9999px;
	padding-top: 9999px;
	padding-bottom: 9999px;
}
.bodyContainer {
	overflow: hidden;
}
</style>
