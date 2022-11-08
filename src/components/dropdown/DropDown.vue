<template>
    <div class="dropdown" ref="mydropdown" @click="dropdownHandler">
        <div class="dropdown_header">
            <div class="circle-button">
                <div class="dot"></div>
                <div class="dot"></div>
                <div class="dot"></div>
            </div>
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

<script>

export default {
  name: 'DropDown',
  data() {
    return {
      currentSort: 'Default',
      isDropdown: false,
    }
  },
  mounted() {
    window.addEventListener('click', this.close)
  },
  beforeUnmount() {
    window.removeEventListener('click', this.close)
  },
  methods: {
    // Закрыть ввыпадающий список по клику снаружи
    close(event) {
      if (!this.$refs.mydropdown.contains(event.target))
        this.isDropdown = false
    },
    // Открыть или закрыть выпадающий список
    dropdownHandler() {
      this.isDropdown = !this.isDropdown
    },
    // Изменить выбор сортировки заметок
    changeSort(type) {
      switch (type.option) {
        case 'Default':
          this.currentSort = 'Default'
          break;
        case 'Date':
          this.currentSort = 'Date'
          break;
        case 'Alphabet':
          this.currentSort = 'Alphabet'
          break;
      }

      // Передаем в родителя объект isSelected
      this.$emit('sortOptionChanged', {
        option: type.option,
      })
    }
  }
}
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