<template>
  <div class="circle-button">
    <slot></slot>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'CircleButton'
})
</script>

<style scoped lang="scss">
@import '../assets/variables.scss';

.circle-button {
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  width: 29px;
  height: 29px;
  left: 457px;
  top: 64px;
  border-radius: 100%;
  border: 1px solid $dirty-orange;
}
</style>
