<template>
  <div v-if="isFetched" class="wrapper">

    <CirclesBackground/>

    <div class="container" v-cloak>

      <!-- Блок со списком заметок -->
      <div class="main-block main-block_notes-list">
        <div class="main-block_header">
          <div class="main-block_header_half">
            <h1>Notes</h1>
          </div>
          <div class="main-block_header_half main-block_header_half_right">

            <!-- Выпадающий список сортировки -->
            <DropDown @sortOptionChanged="sortNotes">
              <template v-slot:dropdown-items="{clickOption: {changeSort}, sort: {currentSort}}">
                <DropdownItem title="Default" :sort="currentSort" @clickOption = "changeSort"/>
                <DropdownItem title="Date" :sort="currentSort" @clickOption = "changeSort"/>
                <DropdownItem title="Alphabet" :sort="currentSort" @clickOption = "changeSort"/>
              </template>
            </DropDown>
    
          </div>
        </div>

        <div class="main-block_search">
          <input @input="searchItem" placeholder="Search...">
        </div>

        <div class="main-block_list">
          <div class="main-block_list_item-cont" v-for:="(note, index) in allNotes">
            <NoteItem 
              :title="note.title" 
              @click="isMobile ? openNote(index) : setCurrentNote(index)"
              :checkBox="isEdit"
              :index="index"
              @changeSelection="updateSelectedList"
            />
          </div>
        </div>

        <div class="main-block_footer">
          <div class="main-block_footer_edit-button" @click="editNotesList">
            <p v-if="!isEdit">
              Edit
            </p>
            <p v-else>
              Cancel
            </p>
          </div>
          <div class="circle-button circle-button_add" @click="addNoteHandler">
            <p>+</p>
          </div>
        </div>
      </div>

      <!-- Блок редактирования -->
      <div class="main-block main-block_text-input-cont">
        <div class="main-block_cont-top" v-if="!isEmpty">
          <div class="main-block_header_half">
            <input 
              placeholder="Enter the title..." 
              type="text" 
              v-model="currentNote.title" 
              @change="checkChanged"/>
          </div>
          <div class="main-block_header_half main-block_header_half_right">
            <p>{{currentNote.date}}</p>
          </div>
        </div>
        <div class="main-block_text-cont" v-if="!isEmpty">
          <textarea 
            v-model="currentNote.value"
            @change="checkChanged"
          ></textarea>
        </div>

        <div class="main-block_footer" id="right-footer" v-if="!isEmpty">
          <div v-if="isMobile" class="circle-button circle-button_back" @click="closeNote">

          </div>
          <div class="circle-button circle-button_delete" @click="deleteNoteHandler">
            <svg width="16" height="22" viewBox="0 0 16 22" fill="none" xmlns="http://www.w3.org/2000/svg" class="delete-icon">
              <path class="main-block_footer_delete-icon"
                d="M4.81818 8.09677L5.45455 16.4839M10.5455 16.4839L11.1818 8.09677M8 8.09677V16.4839M10.5455 4.22581H13.8797C14.4768 4.22581 14.9408 4.74564 14.8733 5.33889L13.1919 20.1131C13.1343 20.6183 12.7068 21 12.1983 21H3.19973C2.67679 21 2.24216 20.5971 2.20259 20.0757L1.08161 5.30146C1.03758 4.72104 1.49665 4.22581 2.07875 4.22581H5.45455M10.5455 4.22581V2C10.5455 1.44772 10.0977 1 9.54545 1H6.45455C5.90226 1 5.45455 1.44772 5.45455 2V4.22581M10.5455 4.22581H5.45455"
                stroke="#D39800" 
                stroke-linecap="round"
              />
            </svg>
          </div>
          
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import NoteItem from './components/NoteItem.vue'
import CirclesBackground from './components/CirclesBackground.vue'
import DropDown from './components/dropdown/DropDown.vue'
import DropdownItem from './components/dropdown/DropdownItem.vue'

const defaultNotes = require('./assets/default_notes')

// Сортировка заметок по алфавиту
function byTitle(title) {
  return (a, b) => a[title] > b[title] ? 1 : -1;
}

// Сортировка по убыванию даты
function byDate(date) {
  return (a, b) => 
    new Date(formateDate(a[date])) > new Date(formateDate(b[date])) ? -1 : 1
}

function formateDate(date) {
  let dd = date.substring(0,3)
  let mm = date.substring(3,6)
  let formatedDate = mm + dd + date.slice(6) + ':00'

  return formatedDate
}

export default {
  name: 'App',
  components: {
    NoteItem,
    CirclesBackground,
    DropDown,
    DropdownItem
  },
  data () {
    return {
      isFetched: false, // Отправлен ли запрос к API
      allNotes: defaultNotes,
      currentNote: defaultNotes[0],
      defaultSorted: [], // Временный список заметок при изменении сортировки
      currentIndex: 0,
      isEmpty: false, // Является ли заметка пустой
      isEdit: false, // Множественный выбор
      itemsForEdit: [], // Выбранные заметки
      search: '', // Подстрока для поиска заметок
      hasChanged: false, // Заметка была изменена
      isMobile: false
    }
  },
  async created() {
    // Создать заметку-пример
    this.allNotes[0].value = await this.generateText()
    // Запрос выполнен
    this.isFetched = true

    // Добавляет сгенерированную заметку-пример в дефолтную сортировку
    this.defaultSorted = [...this.allNotes]

    // Определить мобильная или десктопная версия
    if(window.matchMedia(
        '(max-device-width: 640px)', 
        '(min-device-width: 320px)', 
        '(-webkit-min-device-pixel-ratio: 2)'
      ).matches)
    {
      this.isMobile = true
    }
  },
  methods: {
    // Генератор текста
    async generateText() {
        try {
          let data = await fetch('https://hipsum.co/api/?sentences=25&type=hipster-centric&start-with-lorem=1')
          let jsonData = await data.json()
          let result = jsonData[0]
          return result
        } 
        catch (error) {
          console.log(error)
          return 'Template text'
        }
    },
    // Открыть заметку
    setCurrentNote(index) {
      // Если пустая заметка не изменена, удалить ее
      if(this.currentNote.title.length === 0 && this.currentNote.value.length === 0) {
        this.allNotes.shift()
        this.currentNote = this.allNotes[index-1]
        this.currentIndex = index - 1
      }
      else {

        // Добавить название предыдущей заметки если оно пустое
        if(this.currentNote.title.length === 0) {

          if(this.currentNote.value.length > 10 )
            this.currentNote.title = this.currentNote.value.substring(0,10) + '...'

          if(this.currentNote.title.length === 0 && this.currentNote.value.length <= 10 )
            this.currentNote.title = this.currentNote.value
        }
        
        this.currentNote = this.allNotes[index]
        this.currentIndex = index
      }
        
      this.isEmpty = false
      this.hasChanged = false
    },
    // Добавить новую заметку
    addNoteHandler() {
      if(this.currentNote.value.length !== 0 || this.currentNote.title.length !== 0) {
        let newDate = this.getDate()
        this.allNotes.unshift({title: '', value: '', date: newDate, edited: newDate})
        this.currentNote = this.allNotes[0]
        this.isEmpty = false
        if(this.isMobile)
          this.openNote(this.currentIndex)
      }
    },
    // Удалить заметку
    deleteNoteHandler() {
      // Для оной заметки
      if(!this.isEdit) {
        this.allNotes.splice(this.currentIndex,1)
        this.isEmpty = true
      }
      // Для выбора через edit
      else {
        for (let i = this.itemsForEdit.length -1; i >= 0; i--)
          this.allNotes.splice(this.itemsForEdit[i],1)
        this.isEmpty = true
        this.isEdit = false
      }
      this.defaultSorted = [...this.allNotes]
    },
    // Если новая заметка больше не пустая
    editNotesList() {
      this.isEdit = !this.isEdit
    },
    // Выбрать несколько заметок
    updateSelectedList(isSelected) {
      this.itemsForEdit.push(isSelected.index)
    },
    // Поиск заметки по названию
    searchItem(event) {
      this.allNotes = []
      this.defaultSorted.forEach(item => {
        // Входит ли строка в тайтл какого-либо элемента массива
        if(item.title.toLowerCase().indexOf(event.target.value.toLowerCase()) + 1) {
          this.allNotes.unshift(item)
        }
      })
    },
    // Отсортировать заметки
    sortNotes(type) {
      switch (type.option) {
        case 'Default':
          if(this.allNotes.length > 0)
            this.allNotes.sort(byDate('edited'))
          break;
        case 'Date':
          if(this.allNotes.length > 0)
            this.allNotes.sort(byDate('date'))
          break;
        case 'Alphabet':
          if(this.allNotes.length > 0)
            this.allNotes.sort(byTitle('title'))
          break;
      }
    },
    // Если заметка изменена, переместить ее в начало списка
    checkChanged() {
      if(!this.hasChanged) {
        let forReplace = this.allNotes.splice(this.currentIndex, 1)
        forReplace[0].edited = this.getDate()
        this.allNotes.unshift(forReplace[0])
        this.hasChanged = true
        this.defaultSorted = [...this.allNotes]
        this.setCurrentNote(0)
      }
    },
    // Получить текущую дату
    getDate() {
      let currentDate = new Date();
      let dd = String(currentDate.getDate()).padStart(2, '0')
      let mm = String(currentDate.getMonth() + 1).padStart(2, '0')
      let yy = currentDate.getFullYear().toString().slice(2,4)
      let hrs = String(currentDate.getHours()).padStart(2, '0')
      let min = String(currentDate.getMinutes()).padStart(2, '0')
      let crDate =  dd + '.' + mm + '.' + yy + ' ' + hrs + ':' + min
      return crDate 
    },
    // Открыть заметку в мобильной версии
    openNote(index) {
      let editor = document.querySelector('.main-block_text-input-cont')
      editor.classList.add("text-input-cont-visible")
      this.currentNote = this.allNotes[index]
      this.currentIndex = index
    },
    // Закрыть заметку в мобильной версии
    closeNote() {
      let editor = document.querySelector('.main-block_text-input-cont')
      editor.classList.remove("text-input-cont-visible")

      // Если новая заметка не изменена, удалить её
      if(this.currentNote.title.length === 0 && this.currentNote.value.length === 0)
        this.allNotes.shift()
    }
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@300;400&display=swap');
@import './assets/variables.scss';

body {
  margin: 0;
}

.wrapper {
  @extend %cont-shared;
  position: absolute;
  flex-direction: row;
  height: 100%;
  width: 100%;
  background: linear-gradient(103.84deg, #537FC2 6.25%, #5CC8C1 90.1%);
  overflow: hidden;
}

.container {
  @extend %cont-shared;
  position: absolute;
  margin: 0;
  flex-direction: row;
  height: 100%;
  width: 100%;
  max-width: 3840px;
  background: transparent;
}

.main-block {
  @extend %cont-shared;
  flex-direction: column;
  justify-content: flex-start;
  height: 90.5%;
  background: white;
  border-radius: 20px;
}

.main-block_notes-list {
  width: 30.5%;
  min-width: 160px;
  margin-left: 25px;
  margin-right: 20px;
}

.main-block_header {
  @extend %cont-shared;
  height: 76px;
  width: 100%;
}

.main-block_header_half {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  height: 100%;
  width: 45%;
  user-select: none;

  input {
    @extend %primary-font;
    font-weight: 400;
    font-size: 24px;
    border: none;

    &:focus {
      @extend %primary-font;
      font-weight: 400;
      font-size: 24px;
      outline: none;
    }

    &::placeholder {
      @extend %primary-font;
      font-weight: 300;
      font-size: 24px;
      color: $light-gray;
    }
  }
}

.main-block_header_half_right {
  justify-content: flex-end;

  p {
    @extend %primary-font;
    font-weight: 300;
    font-size: 16px;
    color: $light-gray;
  }
}

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

  &:hover {
    background-color: $dirty-orange;

    .dot {
      background-color: white;
    }
  }
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

.main-block_search {
  @extend %cont-shared;
  width: 92%;
  height: 40px;
  background: $light;
  border-radius: 15px;

  input {
    width: 95%;
    height: 68%;
    background-color: transparent;
    border: none;
    user-select: none;
    font-size: 20px;

    &::placeholder {
      @extend %primary-font;
      font-weight: 300;
      font-size: 20px;
      color: $light-gray;
    }

    &:focus {
      @extend %primary-font;
      outline: none;
      font-weight: 300;
      font-size: 20px;
    }
  }
}

.main-block_list{
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  margin-top: 2%;
  width: 92%;
  height: 75%;
  overflow-y: scroll;
  @extend %custom-scrollbar
}

.main-block_list_item-cont {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: fit-content;
  width: 92%;
  margin-top: 10px;
}

.main-block_footer {
  position: absolute;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  width: 100%;
  height: 45px;
  background-color: white;
  border-radius: 0 0 20px 20px;
  box-shadow: 0px -5px 8px rgba(0, 0, 0, 0.12);
}

.circle-button_add {
  margin-right: 5%;

  p {
    @extend %primary-font;
    font-weight: 400;
    font-size: 24px;
    color: $dirty-orange;
    user-select: none;
  }

  &:hover {
    p {
      color: white;
    }
  }
}

.main-block_footer_edit-button {
  position: absolute;
  display: flex;
  left: 5%;
  cursor: pointer;

  @extend %primary-font;
  font-weight: 300;
  font-size: 20px;
  color: $dirty-orange;
}

/* Правый блок */
.main-block_text-input-cont {
  width: 61%;
  margin-left: 20px;
  margin-right: 25px;
}

.main-block_cont-top {
  @extend %cont-shared;
  width: 100%;
  height: 76px;
}

.main-block_text-cont {
  @extend %cont-shared;
  width: 90%;
  height: 85%;

  textarea {
    width: 100%;
    height: 92%;
    border: none;
    resize: none;
    cursor: auto;
    @extend %custom-scrollbar;

    @extend %primary-font;
    font-weight: 300;
    font-size: 24px;
    line-height: 28px;

    &:focus {
      outline: 0;
    }
  }
}

#right-footer {
  box-shadow: none;
}

.circle-button_delete {
  margin-right: 1%;

  &:hover {
    background-color: red;
    border: 1px solid red;

    .main-block_footer_delete-icon {
      stroke: white;
      fill: red;
    }
  }
}

/* Заголовки */ 
h1 {
  @extend %primary-font;
  font-weight: 400;
  font-size: 30px;
}

h2 {
  @extend %primary-font;
  font-weight: 400;
  font-size: 24px;
}

@media only screen 
  and (min-device-width: 320px) 
  and (max-device-width: 640px)
  and (-webkit-min-device-pixel-ratio: 2) 
{
  .main-block_notes-list {
    position: absolute;
    width: 100%;
    height: 100%;
    margin-left: 0;
    margin-right: 0;
    border-radius: 0;
    z-index: 1;
  }

  .main-block_text-input-cont {
    position: absolute;
    display: none;
    width: 100%;
    height: 100%;
    margin-left: 0;
    margin-right: 0;
    border-radius: 0;
    z-index: 3;
  }

  .text-input-cont-visible {
    display: flex;
  }

  #right-footer {
    justify-content: space-between;
  }

  .circle-button_back {
    margin-left: 5%;
  }
  
  .circle-button_delete {
    margin-right: 5%;
  }

}

</style>
