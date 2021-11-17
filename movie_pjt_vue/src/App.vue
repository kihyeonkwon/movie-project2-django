<template>
  <div id="app">
    <nav id="nav" class="navbar-expand-md align-items-center flex-column fixed-top bg-none">
      <!-- Home 컴포넌트 제작 -->
      <div class="container-fluid d-flex">
        <a href="/" class="navbar-brand">Home</a>
        <!-- Search bar 제작 -->
        <div class="input-group ps-5 ">
          <div id="navbar-search-autocomplete" class="form-outline">
            <input type="search" id="form1" class="form-control" placeholder="Search"/>
          </div>
        </div>
        <!-- 오른쪽 컴포넌트 제작 -->
        <div>
          <ul class="navbar-nav flex-row">
            <li class="nav-item"><router-link to="/"> Home </router-link></li>
            <span class="d-flex" v-if="login">
              <p class="px-2">|</p>
              <li class="nav-item"><router-link to="/accounts/login"> 로그인 </router-link></li>
              <p class="px-2">|</p>
              <li class="nav-item"><router-link to="/accounts/signup"> 회원가입 </router-link></li>
            </span>
            <span v-else>
              <p class="px-2">|</p>
              <li class="nav-item"><router-link @click.native="logout" to="#"> 로그아웃 </router-link></li>
            </span>
          </ul>
        </div>
        <!-- 오른쪽 컴포넌트 마지막 -->
      </div>
    </nav>
    <router-view @login="login = false"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      login: false,
    }
  },
  methods: {
    logout: function () {
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    }
    
  },
  created: function () {
    // 1. Vue instance가 생성된 직후에 호출되어 jwt를 가져오기
    const token = localStorage.getItem('jwt')
    // 2. 토큰이 있다면
    if (token) {
      // 3. true로 변경하고, 없으면 유지한다.
      this.login = true
    }
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  white-space: nowrap;
  padding: auto;
  margin: auto;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
