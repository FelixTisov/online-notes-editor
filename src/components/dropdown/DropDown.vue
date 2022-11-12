<template>
    <div class="dropdown" ref="mydropdown">
        <div class="dropdown_header">
          <CircleButton :class="'circle-buttonw_with-dots'" @click="dropdownHandler">
            <div class="dot"></div>
            <div class="dot"></div>
            <div class="dot"></div>
          </CircleButton>
          <!-- <div class="circle-button" @click="dropdownHandler">
              <div class="dot"></div>
              <div class="dot"></div>
              <div class="dot"></div>
          </div> -->
        </div>
        <div v-if="isDropdown" class="dropdown_body">
            <div class="dropdown_body_drop-title">
                <p>Sort by:</p>
            </div>
            <slot
              name="dropdown-items"
              :sort="{currentSort}"
              :clickOption="{changeSort}"
            ></slot>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import CircleButton from '../CircleButton.vue'

export default defineComponent({
  name: 'DropDown',
  components: {
    CircleButton
  },
  data () {
    return {
      currentSort: 'Default',
      isDropdown: false
    }
  },
  mounted () {
    window.addEventListener('click', this.close)
  },
  beforeUnmount () {
    window.removeEventListener('click', this.close)
  },
  methods: {
    // Закрыть ввыпадающий список по клику снаружи
    close (event:Event) {
      if (!(this.$refs.mydropdown as HTMLDivElement).contains(event.target as Node)) {
        this.isDropdown = false
      }
    },
    // Открыть или закрыть выпадающий список
    dropdownHandler () {
      this.isDropdown = !this.isDropdown
    },
    // Изменить выбор сортировки заметок
    changeSort (option:string) {
      switch (option) {
        case 'Default':
          this.currentSort = 'Default'
          break
        case 'Date':
          this.currentSort = 'Date'
          break
        case 'Alphabet':
          this.currentSort = 'Alphabet'
          break
      }

      // Передаем в родителя объект isSelected
      this.$emit('sortOptionChanged', option)
    }
  }
})
</script>

<style scoped lang="scss">
@import '../../assets/variables.scss';

.dropdown {
  position: absolute;
  display: flex;
  flex-direction: column;
  width: 152px;
  height: fit-content;
  z-index: 5;
}
.dropdown_header {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  width: 100%;
  height: fit-content;
}

.dot {
  position: relative;
  display: block;
  border-radius: 100%;
  margin-left: 2px;
  margin-right: 2px;
  width: 5px;
  height: 5px;
  background: $dirty-orange;
}

.circle-buttonw_with-dots {
  &:hover {
    background-color: $dirty-orange;

    .dot {
      background-color: white;
    }
  }
}
.dropdown_body {
  @extend %cont-shared;
  position: absolute;
  flex-direction: column;
  margin-top: 36px;
  width: 100%;
  height: 132px;
  background-color: white;
  border-radius: 15px;
  box-shadow: 4px 4px 6px rgba(0, 0, 0, 0.15);
}
.dropdown_body_drop-title {
  display: flex;
  align-items: center;
  height: 30px;
  width: 85%;
  border-bottom: 1px solid $light;
}
</style>
