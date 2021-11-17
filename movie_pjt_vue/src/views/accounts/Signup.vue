<template>
  <div>
    <section class="h-100 h-custom" style="background-color: #8fc4b7;">
      <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col-lg-12 col-xl-11">
            <div class="card rounded-3">
              <div class="card-body p-md-5">
                <div class="row justify-content-center">
                  <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">

                    <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Sign up</p>

                    <form class="mx-1 mx-md-4">

                      <div class="d-flex flex-row align-items-center mb-4">
                        <div class="form-outline flex-fill mb-0">
                          <label class="form-label" for="username">Your ID</label>
                          <input type="text" id="username" class="form-control" placeholder="Enter your ID"
                          v-model="credentials.username" />
                        </div>
                      </div>

                      <div class="d-flex flex-row align-items-center mb-4">
                        <div class="form-outline flex-fill mb-0">
                          <label class="form-label" for="last_name">Last Name</label>
                          <input type="text" id="last_name" class="form-control" placeholder="Last Name"
                          v-model="credentials.last_name"/>
                        </div>

                        <div class="form-outline flex-fill mb-0">
                          <label class="form-label" for="first_name">First Name</label>
                          <input type="text" id="first_name" class="form-control" placeholder="First Name"
                          v-model="credentials.first_name"/>
                        </div>
                      </div>

                      <div class="d-flex flex-row align-items-center mb-4">
                        <div class="form-outline flex-fill mb-0">
                          <label class="form-label" for="email">Your Email</label>
                          <input type="email" id="email" class="form-control" placeholder="Enter your Email"
                          v-model="credentials.email"/>
                        </div>
                      </div>

                      <div class="d-flex flex-row align-items-center mb-4">
                        <div class="form-outline flex-fill mb-0">
                          <label class="form-label" for="password">Password</label>
                          <input type="password" id="password" class="form-control" placeholder="Enter your Password"
                          v-model="credentials.password"/>
                        </div>
                      </div>

                      <div class="d-flex flex-row align-items-center mb-4">
                        <div class="form-outline flex-fill mb-0">
                          <label class="form-label" for="passwordConfirmation">Repeat your password</label>
                          <input type="password" id="passwordConfirmation" class="form-control" placeholder="Enter your Password"
                          @keypress.enter="signup(credentials)" v-model="credentials.passwordConfirmation"/>
                        </div>
                      </div>
<!-- 
                      <div class="form-check d-flex justify-content-center mb-5">
                        <input
                          class="form-check-input me-2"
                          type="checkbox"
                          value=""
                          id="form2Example3c"
                        />
                        <label class="form-check-label" for="form2Example3">
                          I agree all statements in <a href="#!">Terms of service</a>
                        </label>
                      </div> -->

                      <div class="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
                        <button @click="signup(credentials)" class="btn btn-primary btn-lg">Register</button>
                      </div>

                    </form>

                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
 name: 'Signup',
 data: function () {
    return {
      credentials: {
        username: '',
        last_name: '',
        first_name: '',
        email: '',
        password: '',
        passwordConfirmation: '',
      }
    }
  },
  methods: {
    signup: function (credentials) {
      console.log(credentials)
      //axios
      axios.post(`${SERVER_URL}/accounts/signup/`, this.credentials)
      .then((res) => {
        console.log(res)
        this.$router.push({ name: 'Home' })
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>