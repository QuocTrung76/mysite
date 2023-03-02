function delete_element(elem) {
    const old_elem = document.getElementById(elem)
    if (old_elem) {
        old_elem.remove()
    }
}

function append_element(elemType, elemId, elemContent, parentElem) {
    const element = document.createElement(elemType);
    if (elemId) {
        element.id = elemId
    }
    const node = document.createTextNode(elemContent);
    if (elemContent) {
        element.appendChild(node);
    }
    parentElem.appendChild(element)
}

$('#search-vocalburaly').on('submit', function(e){
    e.preventDefault();
    $.ajax({
        type:'GET',
        url:url_search,
        data:
        {
            word:$('#word').val(),
            wordFromList:wordFromList,
            tableName:$('#table').val(),
            command: command,
        },
        success:function(data){
            
            if (!data['valid']) {
                if (data['error']) {

                    const translate_content = document.getElementById("translate-content")
                    
                    delete_element('translate-content-text')
                    append_element(elemType='div', elemId="translate-content-text", elemContent=null, translate_content)
                    const translate_text = document.getElementById("translate-content-text")

                    delete_element('error-box')
                    append_element(elemType='p', elemId='error-box', elemContent=data['error'], translate_text)
                }
                command = ""
            } else {
                const translate_content = document.getElementById("translate-content")
                delete_element("translate-content-text")
                append_element(elemType='div', elemId="translate-content-text", elemContent=null, translate_content)
                const translate_text = document.getElementById("translate-content-text")
                
                for (let i = 0; i < data['lexicalCategory'].length; i++) {
                    lexicalCategory = data['lexicalCategory'][i]
                    elemId = 'type-box-' + i
                    delete_element(elemId)
                    append_element(elemType='h4', elemId=elemId, elemContent=lexicalCategory, translate_text)
                    elemId = 'definitions-box-' + i
                    delete_element(elemId)
                    if (Object.keys(data['wordDict'][lexicalCategory]).includes('definitions')) {
                        append_element(elemType='ol', elemId=elemId, elemContent='definitions', parentElem=translate_text)
                        const definitions_text = document.getElementById(elemId)
                        for (let j = 0; j < data['wordDict'][lexicalCategory]['definitions'].length; j++) {
                            definition = data['wordDict'][lexicalCategory]['definitions'][j]
                            elemId = 'definition-box-' + j
                            append_element(elemType='li', elemId=elemId, elemContent=definition, definitions_text)
                        }
                    }
                    elemId = 'examples-box-' + i
                    delete_element(elemId)
                    if (Object.keys(data['wordDict'][lexicalCategory]).includes('examples')) {
                        append_element(elemType='ol', elemId=elemId, elemContent='examples', parentElem=translate_text)
                        const examples_text = document.getElementById(elemId)
                        for (let j = 0; j < data['wordDict'][lexicalCategory]['examples'].length; j++) {
                            example = data['wordDict'][lexicalCategory]['examples'][j]
                            elemId = 'example-box-' + j
                            append_element(elemType='li', elemId=elemId, elemContent=example, examples_text)
                        }
                    }
                    elemId = 'synonyms-box-' + i
                    delete_element(elemId)
                    if (Object.keys(data['wordDict'][lexicalCategory]).includes('synonyms')) {
                        append_element(elemType='ol', elemId=elemId, elemContent='synonyms', parentElem=translate_text)
                        const synonyms_text = document.getElementById(elemId)
                        for (let j = 0; j < data['wordDict'][lexicalCategory]['synonyms'].length; j++) {
                            synonym = data['wordDict'][lexicalCategory]['synonyms'][j]
                            elemId = 'synonym-box-' + j
                            append_element(elemType='li', elemId=elemId, elemContent=synonym, synonyms_text)
                        }
                    }
                }

                if (command == "Add") {
                    var oldWord = document.getElementById("words-list")
        
                    oldWord.innerHTML = ""

                    data['wordList'].forEach(element => {
                        append_element(elemType='li', elemId=element, elemContent="", oldWord)
                        let parent_li = document.getElementById(element)
                        word_id = element + "-word"
                        append_element(elemType='button', elemId=word_id, elemContent=element, parent_li)
                        word_button = document.getElementById(word_id)
                        word_button.setAttribute('type', 'button')
                        word_button.setAttribute('value', element)
                    });
                    setNewWordList[data['tableName']] = data['wordList'];
                }
                command = ""
            }
        }
    })
});

$('#search-vocalburaly-from-list').on('click', 'button', function(e){
    e.preventDefault();
    $.ajax({
        type:'GET',
        url:url_search,
        data:
        {
            wordFromList:wordFromList,
            tableName:$('#table').val(),
            command: command,
        },
        success:function(data){
            
            if (!data['valid']) {
                if (data['error']) {

                    const translate_content = document.getElementById("translate-content")
                    
                    delete_element('translate-content-text')
                    append_element(elemType='div', elemId="translate-content-text", elemContent=null, translate_content)
                    const translate_text = document.getElementById("translate-content-text")

                    delete_element('error-box')
                    append_element(elemType='p', elemId='error-box', elemContent=data['error'], translate_text)
                }
                command = ""
            } else {
                const translate_content = document.getElementById("translate-content")
                delete_element("translate-content-text")
                append_element(elemType='div', elemId="translate-content-text", elemContent=null, translate_content)
                const translate_text = document.getElementById("translate-content-text")
                
                for (let i = 0; i < data['lexicalCategory'].length; i++) {
                    lexicalCategory = data['lexicalCategory'][i]
                    elemId = 'type-box-' + i
                    delete_element(elemId)
                    append_element(elemType='h4', elemId=elemId, elemContent=lexicalCategory, translate_text)
                    elemId = 'definitions-box-' + i
                    delete_element(elemId)
                    if (Object.keys(data['wordDict'][lexicalCategory]).includes('definitions')) {
                        append_element(elemType='ol', elemId=elemId, elemContent='definitions', parentElem=translate_text)
                        const definitions_text = document.getElementById(elemId)
                        for (let j = 0; j < data['wordDict'][lexicalCategory]['definitions'].length; j++) {
                            definition = data['wordDict'][lexicalCategory]['definitions'][j]
                            elemId = 'definition-box-' + j
                            append_element(elemType='li', elemId=elemId, elemContent=definition, definitions_text)
                        }
                    }
                    elemId = 'examples-box-' + i
                    delete_element(elemId)
                    if (Object.keys(data['wordDict'][lexicalCategory]).includes('examples')) {
                        append_element(elemType='ol', elemId=elemId, elemContent='examples', parentElem=translate_text)
                        const examples_text = document.getElementById(elemId)
                        for (let j = 0; j < data['wordDict'][lexicalCategory]['examples'].length; j++) {
                            example = data['wordDict'][lexicalCategory]['examples'][j]
                            elemId = 'example-box-' + j
                            append_element(elemType='li', elemId=elemId, elemContent=example, examples_text)
                        }
                    }
                    elemId = 'synonyms-box-' + i
                    delete_element(elemId)
                    if (Object.keys(data['wordDict'][lexicalCategory]).includes('synonyms')) {
                        append_element(elemType='ol', elemId=elemId, elemContent='synonyms', parentElem=translate_text)
                        const synonyms_text = document.getElementById(elemId)
                        for (let j = 0; j < data['wordDict'][lexicalCategory]['synonyms'].length; j++) {
                            synonym = data['wordDict'][lexicalCategory]['synonyms'][j]
                            elemId = 'synonym-box-' + j
                            append_element(elemType='li', elemId=elemId, elemContent=synonym, synonyms_text)
                        }
                    }
                }
                command = ""
            }
        }
    })
});