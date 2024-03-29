import ServiceBase from "../base/serviceBase";
import {FieldOfStudyDTO, mapFieldOfStudyDTOToModel} from "../dto/fieldOfStudyDTO";
import fetchFieldsOfStudy from "../../api/fetchFieldsOfStudy";
import {UniversityDTO} from "../dto/universityDTO";
import {fieldOfStudies} from "../../helpers/mock";

export class FieldOfStudyService extends ServiceBase {
    async fetchData(offset, count) {
        //const fieldsJSON = await fetchFieldsOfStudy(offset, count);

        //return fieldsJSON.map(json => Object.assign(new FieldOfStudyDTO(), json))

        if (offset > 2) {
            return new Promise(resolve => resolve([]));
        }

        return new Promise((resolve) => {
            setTimeout(() => {
                resolve([new FieldOfStudyDTO('01.02.03', "Field1"), new UniversityDTO('04.05.06', "Field2")])
            }, 1000)
        });
    }

    load() {
        this.store.setNewItems(fieldOfStudies);
    }

    getFieldOfStudyModel(id) {
        return this.store.items.find(fieldOfStudy => fieldOfStudy.id === id);
    }

    mapDTOToModel(dto) {
        return mapFieldOfStudyDTOToModel(dto);
    }
}