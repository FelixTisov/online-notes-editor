<template>
  <button>
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

    &:hover {
        background: linear-gradient(90deg, #06D2FF 0%, #DB00FF 100%);
    }
}

</style>
