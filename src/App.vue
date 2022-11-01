<template>
  <div v-if="isFetched" class="wrapper">

    <CirclesBackground/>

    <div class="container" v-cloak>
      <div class="main-block notes-list-cont">

        <div class="header">
          <div class="header-half">
            <h1>Notes</h1>
          </div>
          <div class="header-half right-half">
            <div class="circle-button">
              <div class="dot"></div>
              <div class="dot"></div>
              <div class="dot"></div>
            </div>
          </div>
        </div>

        <div class="search">
          <input placeholder="Search..."/>
        </div>

        <div class="items-cont" v-for:="(note, index) in allNotes">
          <NoteItem 
            :title="note.title" 
            @click="setCurrentNote(index)"
            :checkBox="isEdit"
            :index="index"
            @changeSelection="updateSelectedList"
            
          />
        </div>

        <div class="footer">
          <div class="edit-button" @click="editNotesList">
            <p v-if="!isEdit">
              Edit
            </p>
            <p v-else>
              Cancel
            </p>
          </div>
          <div class="circle-button add-button" @click="addNoteHandler">
            <p>+</p>
          </div>
          
        </div>
      </div>

      <div class="main-block text-input-cont">
        <div class="cont-top" v-if="!isEmpty">
          <div class="header-half">
            <input placeholder="Enter the title..." type="text" v-model="currentNote.title"/>
          </div>
          <div class="header-half right-half">
            <p>{{currentNote.date}}</p>
          </div>
        </div>
        <div class="text-cont" v-if="!isEmpty">
          <textarea v-model="currentNote.value"></textarea>
        </div>

        <div class="footer" id="right-footer" v-if="!isEmpty">
          <div class="circle-button delete-button" @click="deleteNoteHandler">
            <svg width="16" height="22" viewBox="0 0 16 22" fill="none" xmlns="http://www.w3.org/2000/svg" class="delete-icon">
              <path class="delete-icon"
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

const defaultNotes = require('./components/default_notes')

export default {
  name: 'App',
  components: {
    NoteItem,
    CirclesBackground
  },
  data () {
    return {
      isFetched: false,
      allNotes: defaultNotes,
      currentNote: defaultNotes[0],
      currentIndex: 0,
      isEmpty: false,
      isEdit: false, // Множественный выбор
      itemsForEdit: [], // Выбранные заметки
      newAdded: false
    }
  },
  async created() {
    async function generateText() {
        try {
            let data = await fetch('https://hipsum.co/api/?sentences=5&type=hipster-centric&start-with-lorem=1')
            let jsonData = await data.json()
            let result = jsonData[0]
            return result
        } catch (error) {
            console.log(error)
            return 'Template text'
        }
    }

    this.allNotes[0].value = await generateText()
    // Если запрос завершился
    this.isFetched = true
  },
  methods: {
    setCurrentNote(index) {
      
      // Если пустая заметка не изменена, удалить ее
      if(this.currentNote.title.length === 0 && this.currentNote.value.length === 0) {
        this.allNotes.shift()
        this.currentNote = this.allNotes[index-1]
        this.currentIndex = index - 1
      }
      else {
        this.currentNote = this.allNotes[index]
        this.currentIndex = index
      }
      this.isEmpty = false
      
    },
    addNoteHandler() {
      if(this.currentNote.value.length !== 0 || this.currentNote.title.length !== 0) {
        this.allNotes.unshift({title: '', value: '', date: this.getDate()})
        this.currentNote = this.allNotes[0]
        this.isEmpty = false
      }
    },
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
    },
    editNotesList() {
      this.isEdit = !this.isEdit
    },
    updateSelectedList(isSelected) {
      this.itemsForEdit.push(isSelected.index)
    },
    getDate() {
      let currentDate = new Date();
      let dd = String(currentDate.getDate()).padStart(2, '0')
      let mm = String(currentDate.getMonth() + 1).padStart(2, '0')
      let yy = currentDate.getFullYear().toString().slice(2,4)
      let hrs = String(currentDate.getHours()).padStart(2, '0')
      let min = String(currentDate.getMinutes()).padStart(2, '0')
      currentDate =  dd + '.' + mm + '.' + yy + ' ' + hrs + ':' + min
      return(currentDate)
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@300;400&display=swap');

body {
  margin: 0;
}

.wrapper {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  position: absolute;
  height: 100%;
  width: 100%;
  background: linear-gradient(103.84deg, #537FC2 6.25%, #5CC8C1 90.1%);
  overflow: hidden;
}

.container {
  margin: 0;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  position: absolute;
  height: 100%;
  width: 100%;
  max-width: 3840px;
  background: transparent;
}

.main-block {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  height: 90.5%;
  background: #FFFFFF;
  border-radius: 20px;

}

.notes-list-cont {
  width: 30.5%;
  margin-left: 25px;
  margin-right: 20px;
}

.text-input-cont {
  width: 61%;
  margin-left: 20px;
  margin-right: 25px;
}

.header {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 76px;
  width: 100%;
}

.header-half {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  height: 100%;
  width: 45%;
  /* border: 1px solid black; */
}

.header-half input {
  font-family: 'Rubik';
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  color: #000;
}

.header-half input:focus {
  font-family: 'Rubik';
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  color: #000;
  outline: none;
}

.header-half input::placeholder {
  font-family: 'Rubik';
  font-style: normal;
  font-weight: 300;
  font-size: 24px;
  color: #8A8A8A;
}

.right-half {
  justify-content: flex-end;
}

.right-half p {
  font-family: 'Rubik';
  font-style: normal;
  font-weight: 300;
  font-size: 16px;
  color: #8A8A8A;
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
  border: 1px solid #D39800;
}

.circle-button:hover {
  background-color: #D39800;
}

.circle-button:hover .dot {
  background-color: #fff;
}

.dot {
  position: relative;
  display: block;
  border-radius: 100%;
  margin-left: 2px;
  margin-right: 2px;
  width: 5px;
  height: 5px;
  background: #D39800;
}

.search {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 92%;
  height: 40px;
  background: #ECECEC;
  border-radius: 15px;
}

input {
  width: 95%;
  height: 68%;
  background-color: transparent;
  border: none;
  user-select: none;
  font-size: 20px;
}

input::placeholder {
  font-family: 'Rubik';
  font-style: normal;
  font-weight: 300;
  font-size: 20px;
  color: #8A8A8A;
}

input:focus {
  outline: none;
  font-family: 'Rubik';
  font-style: normal;
  font-weight: 300;
  font-size: 20px;
  color: #000;
}

.items-cont {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: fit-content;
  width: 92%;
  margin-top: 10px;
}

.footer {
  position: absolute;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  width: 100%;
  height: 45px;
  background-color: #fff;
  border-radius: 0 0 20px 20px;
  box-shadow: 0px -5px 8px rgba(0, 0, 0, 0.12);
}

.add-button {
  margin-right: 5%;
}

.add-button:hover p {
  color: #fff;
}

.add-button p {
  font-family: 'Rubik';
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  color: #D39800;
  user-select: none;
}

.edit-button {
  position: absolute;
  display: flex;
  left: 5%;
  cursor: pointer;

  font-family: 'Rubik';
  font-style: normal;
  font-weight: 300;
  font-size: 20px;
  color: #D39800;
}

/* Правый блок */
.cont-top {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 76px;
}

.text-cont {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 90%;
  height: 85%;
}

textarea {
  width: 100%;
  height: 100%;
  border: none;
  resize: none;
  
  font-family: 'Rubik';
  font-style: normal;
  font-weight: 300;
  font-size: 24px;
  line-height: 28px;
  color: #000;
}

textarea:focus {
  outline: 0;
}

#right-footer {
  box-shadow: none;
}

.delete-button {
  margin-right: 1%;
}

.delete-button:hover {
  background-color: red;
  border: 1px solid red;
}

.delete-button:hover .delete-icon {
  stroke: white;
  fill: red;
}

.material-symbols-outlined {
  font-variation-settings:
  'FILL' 0,
  'wght' 400,
  'GRAD' 0,
  'opsz' 48
}

h1 {
  font-family: 'Rubik';
  font-style: normal;
  font-weight: 400;
  font-size: 30px;
  color: #000;
}

h2 {
  font-family: 'Rubik';
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  color: #000;
}

</style>
