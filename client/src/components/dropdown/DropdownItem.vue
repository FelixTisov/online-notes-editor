<template>
  <div :class="{'drop-item': true, 'drop-item_current': sort === title}" @click="changeSort(title)">
    <p>{{title}}</p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'DropdownItem',
  methods: {
    changeSort (option:string | undefined) {
      this.$emit('clickOption', option)
    }
  },
  props: {
    title: String,
    sort: String
  }
})
</script>

<style scoped lang="scss">
@import '../../assets/variables.scss';

.drop-item {
  display: flex;
  align-items: center;
  height: 30px;
  width: 85%;
  cursor: pointer;
  border-radius: 5px;
  padding-left: 4px;

  &:hover {
    background-color: #f3f3f3;
  }

  p {
    @extend %primary-font;
    font-weight: 300;
    font-size: 16px;
    color: #000;
  }
}

.drop-item_current {
  p{
    color: #888;
  }
}
</style>
