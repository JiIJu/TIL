<template>
  <nav>
      <div>
      <router-link to="/" style="text-decoration:none;"><h1>모든</h1></router-link><br>
      <router-link to="/today" style="text-decoration:none;"><h1>오늘</h1></router-link><br>
      <router-link to="/important" style="text-decoration:none;"><h1>중요</h1></router-link>
      </div>
    </nav>
</template>

<script>
export default {
  name : 'SideBar'
}
</script>

<style>

</style>