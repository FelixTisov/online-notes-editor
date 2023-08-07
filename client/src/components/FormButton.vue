<template>
  <button type="submit">
    <slot></slot>
  </button>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'FormButton'
})
</script>

<style lang="scss">
@import '../assets/variables.scss';

button {
    width: 205px;
    height: 40px;
    background: linear-gradient(90deg, #DB00FF 0%, #06D2FF 100%);
    border-radius: 13px;
    border: none;
    cursor: pointer;

    @extend %primary-font;
    font-size: 22px;
    color: #fff;

    &:hover, &:active {
        background: linear-gradient(90deg, #06D2FF 0%, #DB00FF 100%);
    }
}

/* Для мобильной версии */
@media only screen
  and (min-device-width: 320px)
  and (max-device-width: 640px)
  and (-webkit-min-device-pixel-ratio: 2)
{
  button {
    &:hover {
      background: linear-gradient(90deg, #DB00FF 0%, #06D2FF 100%);
    }
  }
}

</style>
