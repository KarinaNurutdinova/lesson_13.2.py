from candidates_dao import CandidatesDAO


candidates_dao = CandidatesDAO()
candidates_all = candidates_dao.get_all()
candidate_one = candidates_dao.get_by_id(1)
candidate_python = candidates_dao.get_by_skill("python")
