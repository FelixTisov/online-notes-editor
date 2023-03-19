<template>
  <div class="wrapper">

    <CirclesBackground/>

    <div class="login-cont">
      <div class="title">
        <p>Login</p>
      </div>

      <form @submit.prevent="login">
        <input v-model="form.email" placeholder="Email"/>
        <input v-model="form.password" placeholder="Password"/>

        <FormButton class="login-btn" >LOGIN</FormButton>
      </form>

      <div class="options">
        <p>Don't have an account?</p>
        <router-link to="/signup"><a class="signup-btn">Sign Up</a></router-link>
      </div>

    </div>

  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import CirclesBackground from '../components/CirclesBackground.vue'
import FormButton from '@/components/FormButton.vue'

interface logindata {
  email: string,
  password: string
}

export default defineComponent({
  name: 'LogIn',
  components: {
    CirclesBackground,
    FormButton
  },
  data () {
    return {
      form: { email: 'userone@gmail.com', password: 'user1' } as logindata
    }
  },
  methods: {
    // Авторизация пользователя
    async login () {
      try {
        const request = new Request(`${process.env.VUE_APP_API_URL}/users/login`,
          {
            method: 'POST',
            body: JSON.stringify({ ...this.form }),
            headers: { 'content-type': 'application/json' }
          }
        )

        fetch(request)
          .then((response) => {
            if (response.status === 303) {
              response.json().then((data) => {
                const userID = data.userid
                const authToken = data.token

                localStorage.setItem('userID', userID)
                localStorage.setItem('authToken', authToken)

                return this.$router.push({ name: 'home' })
              })
            } else {
              throw new Error('Server error!')
            }
          })
          .catch((error) => {
            console.error(error)
          })
      } catch (error) {
        console.log(error)
      }
    }
  }
})
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@300;400&display=swap');
@import '../assets/variables.scss';

body {
  margin: 0;
}

.wrapper {
  @extend %cont-shared;
  position: absolute;
  height: 100%;
  width: 100%;
  background: linear-gradient(103.84deg, #537FC2 6.25%, #5CC8C1 90.1%);
  overflow: hidden;
}

.login-cont {
  @extend %cont-shared;
  flex-direction: column;
  width: 520px;
  height: 500px;
  background: #fff;
  border-radius: 17px;
}

.title {
  @extend %cont-shared;
  height: 70px;
  width: 100%;

  p {
    @extend %primary-font;
    font-size: 40px;
  }
}

form {
  @extend %cont-shared;
  flex-direction: column;
  height: 260px;
  width: 100%;
}

input {
  width: 340px;
  height: 44px;
  background: #ECECEC;
  border-radius: 15px;
  margin-top: 14px;
  margin-bottom: 14px;
  border: none;
  font-size: 16px;
  padding-left: 10px;

  &::placeholder {
    font-size: 16px;
  }

  &:focus{
    outline: none;
  }
}

.login-btn {
  margin-top: 26px;
}

.options {
  @extend %cont-shared;
  flex-direction: column;
  width: 100%;
  height: 50px;
  margin-top: 16px;

  @extend %primary-font;
  font-weight: 300;
  font-size: 15px;

  p {
    margin-top: 3px;
    margin-bottom: 4px;
  }

  .signup-btn {
    margin-top: 4px;
    margin-bottom: 3px;
    color: #9542FF;
    cursor: pointer;
  }
}

/* Для мобильной версии */
@media only screen
  and (min-device-width: 320px)
  and (max-device-width: 640px)
  and (-webkit-min-device-pixel-ratio: 2)
{

  .login-cont {
    max-width: 640px;
    width: 100%;
    min-width: 320px;
    height: 100%;
    border-radius: 0;
  }

  input {
    max-width: 280px;
    min-width: 280px;
  }
}

</style>
