<template>
    <div class="note-item-cont">

        <div class="check-box" v-if="checkBox">
            <div @click="selectItem" :class="this.isSelected ? 'selected' : 'not-selected'"></div>
        </div>
    
        <div class="item-cont">
            <div class="title-cont">
                <h2>{{title}}</h2>
            </div>
            <div class="line"></div>
        </div>

    </div>
</template>

<script>
export default {
  name: 'NoteItem',
  data() {
    return {
        isSelected: false,
    }
  },
  methods: {
    selectItem() {
        this.isSelected = !this.isSelected
        // Передаем в родителя объект isSelected
        this.$emit('changeSelection', {
            value: this.isSelected,
            index: this.index
        })
    },
    cancelSelection() {
        this.isSelected = false
    }
  },
  props: {
    title: String,
    checkBox: Boolean,
    index: Number,
  },
  watch: {
    checkBox(newVal) {
        if(newVal === false)
            this.isSelected = newVal
    }
  }
}
</script>

<style scoped>
.note-item-cont {
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    height: 56px;
    width: 100%;
}
.check-box {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 28px;
    height: 56px;
}

.not-selected{
    margin-top: 25%;
    display: block;
    width: 10px;
    height: 10px;
    cursor: pointer;
    border-radius: 100%;
    border: 1px solid #dedede;
}

.selected{
    margin-top: 25%;
    display: block;
    width: 10px;
    height: 10px;
    cursor: pointer;
    border-radius: 100%;
    border: none;
    background-color: blue;
}

.item-cont {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border-radius: 15px;
    height: 56px;
    width: 100%;
    cursor: pointer;
}

.item-cont:hover {
    box-shadow: 4px 1px 7px rgba(0, 0, 0, 0.15);
}

.item-cont:hover h2 {
    font-size: 25px;
}

.title-cont {
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    height: 99%;
    width: 95%;
}

h2 {
    font-family: 'Rubik';
    font-style: normal;
    font-weight: 300;
    font-size: 24px;
    line-height: 28px;
    color: #000000;
}

.line {
    display: flex;
    position: relative;
    width: 95%;
    height: 1.5px;
    background-color: #ECECEC;
}
</style>