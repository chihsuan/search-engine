class DocLookupsController < ApplicationController

  def index
    
  end

  def show
    doc_id = DocLookup.get_doc(params[:id])
    @document = Document.find(doc_id) 
  end

  def search
    @documents = DocLookup.look_up(params[:keyword])
    render :search_result 
  end

  def search_result
  end

end
