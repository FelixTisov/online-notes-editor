<template>
    <div class="wrapper">

        <CirclesBackground/>

        <div class="signup-cont">
            <div class="title">
                <p>Sign up</p>
            </div>

            <form @submit.prevent="signup">
                <input required v-model="form.userName" placeholder="Your name"/>
                <input required v-model="form.email" placeholder="Email"/>
                <input required v-model="form.password" placeholder="Password"/>

                <FormButton class="login-btn">SIGNUP</FormButton>
            </form>

            <div class="options">
                <p>Already have an account?</p>
                <router-link to="/login"><a class="signup-btn">Log In</a></router-link>
            </div>
        </div>

    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import CirclesBackground from '../components/CirclesBackground.vue'
import FormButton from '@/components/FormButton.vue'

interface signupdata {
  email: string,
  password: string,
  userName: string
}

export default defineComponent({
  name: 'SignUp',
  components: {
    CirclesBackground,
    FormButton
  },
  data () {
    return {
      form: { email: '', password: '', userName: '' } as signupdata
    }
  },
  methods: {
    // Регистрация пользователя
    async signup () {
      try {
        const date = this.getDate()
        const request = new Request(`${process.env.VUE_APP_API_URL}/users/signup`,
          {
            method: 'POST',
            body: JSON.stringify({ ...this.form, date: date }),
            headers: { 'content-type': 'application/json' }
          }
        )

        fetch(request)
          .then((response) => {
            if (response.status === 201) {
              return this.$router.push('/login')
            } else {
              throw new Error('Server error!')
            }
          })
          .catch((error) => {
            console.error(error)
          })
      } catch (error) {
        console.error(error)
      }
    },
    // Получить текущую дату
    getDate () {
      const currentDate = new Date()
      const dd = String(currentDate.getDate()).padStart(2, '0')
      const mm = String(currentDate.getMonth() + 1).padStart(2, '0')
      const yy = currentDate.getFullYear().toString().slice(2, 4)
      const hrs = String(currentDate.getHours()).padStart(2, '0')
      const min = String(currentDate.getMinutes()).padStart(2, '0')
      const crDate = dd + '.' + mm + '.' + yy + ' ' + hrs + ':' + min
      return crDate
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

.signup-cont {
  @extend %cont-shared;
  flex-direction: column;
  width: 520px;
  height: 545px;
  background: #fff;
  border-radius: 17px;
}

.title {
  @extend %cont-shared;
  height: 70px;
  margin-top: -10px;
  width: 100%;

  p {
    @extend %primary-font;
    font-size: 40px;
  }
}

form {
  @extend %cont-shared;
  flex-direction: column;
  height: 330px;
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

  .signup-cont {
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
